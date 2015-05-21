# TA-user-agents

## Overview
This TA provides and external Python lookup that parses User Agents strings, such as those found in Web or Proxy logs.

## Installation
To install:
1. Untar the tarball file in your $SPLUNK_HOME/etc/apps
   directory.
2. Restart Splunk.

## Usage
The lookup expects a field in the events (http_user_agent). Once that field exists (via extractions, alias or rename). Once that field exists, you can use it in a lookup command, as such:
    index=web_proxy | lookup user_agents http_user_agent
The lookup will output the following fields:
  * ua_os_family: The name of the client OS.
  * ua_os_major: The major version of the client OS.
  * ua_os_minor: The minor version of the client OS.
  * ua_os_patch: The patch version of the client OS.
  * ua_os_patch_minor: The minor patch version of the client OS.
  * ua_family: The name of the UA ("Firefox", "IE")
  * ua_major: The major version of the UA.
  * ua_minor: The minor version of the UA.
  * ua_patch: The patch version of the UA
  * ua_device: The type of device used in the event.

## Customization
To add your own user agents, you can use the YAML file in TA-user-agents/bin/ua_parser/ named regexes.yaml.

## Credits
This TA uses a Python module from:

https://github.com/tobie/ua-parser

