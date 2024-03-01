# cdpop

Pop open cash drawer using http or https GET request:

	GET /status	Return cash drawer status
	GET /open	Request cash drawer open

If authentication is configured, supply user and/or auth
as query parameters, eg:

	GET /status?auth=Ricim8Knak

Requests to open drawer will return successfully (200) as
soon as possible, but will be processed in turn once access
to the attached device is available. No feedback is provided for
an open request.

Requests for status will block until a valid status can be read
from the attached device. In the case of a hardware error,
status requests will return Internal Server Error (500).

## Usage

	$ cdpop [config.json]

## Requirements

   - python >= 3.9
   - tornado
   - posiflex-hidcd

## Configuration

Copy example config to a new file and edit as required.
Available configuration options:

   - port (int) TCP service port, default: 41514 (optional)
   - host (string) Listen address, default: "localhost" (optional)
   - cert (string) TLS certificate path, default: None (optional)
   - key (string) TLS private key path, default: None (optional)
   - auth (string) Authorisation key, default: None (optional)
   - user (string) Authorisation username, default: None (optional)
   - drawer (int) Cash drawer number, default: None (optional)

Notes:

   - If drawer number is not specified, cdpop will connect to
     the first hid cash drawer found. See related project
     [posiflex-hidcd](https://github.com/ndf-zz/posiflex-hidcd)
     for details.
   - To listen on all addresses, specify the empty string "" for host.


## MacOS Installation

Install xcode developer tools:

	$ xcode-select --install

Install brew according to [brew website](https://brew.sh/).

Install hidapi using brew:

	$ brew install hidapi

Install python3 if not already installed:

	$ brew install python@3.12

Using python, create a venv and install cdpop packages using pip:

	$ python3 -m venv cdpop --system-site-packages
	$ ./cdpop/bin/pip install cdpop

Optionally, create a cdpop config file.

Create launch agent plist file (see example cdpop.plist),
copy to ~/Library/LaunchAgents and enable using launchctl:

	$ cp cdpop.plist /Library/LaunchAgents
	$ launchctl load ~/Library/LaunchAgents/cdpop.plist
	$ launchctl enable xxx/yyy/cdpop
	$ launchctl kickstart -k xxx/yyy/cdpop
