# SPDX-License-Identifier: MIT
"""Cash Drawer Opener"""

import asyncio
import ssl
import tornado.web
import json
import sys
from time import sleep
from hidcd import HidCd
from logging import getLogger, DEBUG, INFO, WARNING, basicConfig
from signal import SIGTERM

basicConfig(level=INFO)
_log = getLogger('cdpop')
_log.setLevel(INFO)

VERSION = '1.0.0'
SITENAME = 'cdpop'
CSP = "frame-ancestors 'none'; img-src data: 'self'; default-src 'self'"
OPENTRIES = 3


class Application(tornado.web.Application):

    def __init__(self, site):
        handlers = [
            (r"/(.*)", DrawerHandler, dict(site=site)),
        ]
        settings = dict(
            site_version=VERSION,
            site_name=SITENAME,
            autoreload=False,
            serve_traceback=False,
            debug=True,
        )
        super().__init__(handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self, site):
        self._site = site

    def set_default_headers(self, *args, **kwargs):
        self.set_header("Content-Security-Policy", CSP)
        self.set_header("Strict-Transport-Security", "max-age=31536000")
        self.set_header("X-Frame-Options", "deny")
        self.set_header("X-Content-Type-Options", "nosniff")
        self.set_header("X-Permitted-Cross-Domain-Policies", "none")
        self.set_header("Referrer-Policy", "no-referrer")
        self.set_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.set_header("Cross-Origin-Opener-Policy", "same-origin")
        self.set_header("Cross-Origin-Resource-Policy", "same-origin")
        self.clear_header("Server")


class DrawerHandler(BaseHandler):

    async def get(self, path):
        if self.get_argument('auth', None) != self._site.config['auth']:
            _log.warning('Invalid auth')
            raise tornado.web.HTTPError(401)
        if self.get_argument('user', None) != self._site.config['user']:
            _log.warning('Invalid user')
            raise tornado.web.HTTPError(401)

        if path == 'status':
            closed = await self._site.getClosed()
            self.write('closed\n' if closed else 'open\n')
        elif path == 'open':
            await self._site.requestOpen()
            self.write('open requested\n')
        else:
            raise tornado.web.HTTPError(404)


class CdPop:

    def __init__(self):
        self._shutdown = None
        self._lock = asyncio.Lock()
        self._bgr = set()
        self._cd = None
        self.config = {
            'host': 'localhost',
            'port': 41514,
            'cert': None,
            'key': None,
            'auth': None,
            'user': None,
            'drawer': None,
        }

    def connected(self):
        """Return drawer connection status"""
        return self._cd is not None and self._cd.connected()

    def _sigterm(self):
        """Handle TERM signal"""
        _log.warning('Site terminated by SIGTERM')
        self._shutdown.set()

    def drawerConnect(self):
        """Attempt to reconnect drawer in case of error"""
        if not self.connected():
            self._cd = HidCd(self.config['drawer'])
            _log.info('Cash drawer: %r', self._cd.cdnum)

    def drawerClosed(self):
        """Return cash drawer status"""
        try:
            self.drawerConnect()
            return self._cd.closed()
        except Exception as e:
            _log.error('drawerClosed %s: %s', e.__class__.__name__, e)
            self._cd = None
            raise

    def openDrawer(self):
        """Blocking function to perform cash drawer open"""
        try:
            self.drawerConnect()
            count = 0
            while self._cd.closed():
                count += 1
                if count > OPENTRIES:
                    sleep(1.0)
                    break
                if count > 1:
                    _log.info('Open re-try %d', count)
                self._cd.open()
                sleep(1.0)
        except Exception as e:
            _log.error('openDrawer %s: %s', e.__class__.__name__, e)
            self._cd = None

    async def getClosed(self):
        """Return drawer closed status"""
        async with self._lock:
            return await asyncio.get_running_loop().run_in_executor(
                None, self.drawerClosed)

    async def doOpen(self):
        async with self._lock:
            await asyncio.get_running_loop().run_in_executor(
                None, self.openDrawer)

    async def requestOpen(self):
        task = asyncio.create_task(self.doOpen())
        self._bgr.add(task)
        task.add_done_callback(self._bgr.discard)

    def load(self, configFile=None):
        """Read config"""
        if configFile is not None:
            with open(configFile) as f:
                cf = json.load(f)
                if 'port' in cf and cf['port'] is not None:
                    self.config['port'] = int(cf['port'])
                    nv = None
                    try:
                        nv = int(cf['port'])
                    except Exception:
                        _log.warning('Ignored invalid port number')
                    self.config['port'] = nv
                if 'drawer' in cf and cf['drawer'] is not None:
                    nv = None
                    try:
                        nv = int(cf['drawer'])
                    except Exception:
                        _log.warning('Ignored invalid drawer number')
                    self.config['drawer'] = nv
                if 'host' in cf:
                    if cf['host'] is not None:
                        self.config['host'] = cf['host']
                if 'cert' in cf:
                    self.config['cert'] = cf['cert']
                if 'key' in cf:
                    self.config['key'] = cf['key']
                if 'user' in cf:
                    self.config['user'] = cf['user']
                if 'auth' in cf:
                    self.config['auth'] = cf['auth']
        self.drawerConnect()

    async def run(self):
        """Run site in asyncio main loop"""
        self._shutdown = asyncio.Event()
        asyncio.get_running_loop().add_signal_handler(SIGTERM, self._sigterm)
        app = Application(self)
        ssl_ctx = None
        if self.config['cert'] and self.config['key']:
            ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_ctx.load_cert_chain(self.config['cert'], self.config['key'])
        srv = tornado.httpserver.HTTPServer(app, ssl_options=ssl_ctx)
        srv.listen(self.config['port'], self.config['host'])
        _log.info('Listening on: http%s://%s:%s', 's' if ssl_ctx else '',
                  self.config['host'], self.config['port'])
        await self._shutdown.wait()


def main():
    configFile = None
    if len(sys.argv) == 2:
        configFile = sys.argv[1]

    cd = CdPop()
    cd.load(configFile)

    if not cd.connected():
        _log.warning('Cash Drawer not connected')

    return asyncio.run(cd.run())


if __name__ == "__main__":
    sys.exit(main())
