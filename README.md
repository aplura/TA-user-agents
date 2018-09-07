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
To add your own user agents, you can use the YAML file in TA-user-agents/bin/uap-core/ named regexes.yaml.

## Refreshing the BrowserScope database

While any customizations you want can be made, the most frequent request is simply to pull down the latest browser definitions.  Therefore an [automatic update script][fetch-latest] is available in the GitHub repo.

Download the script and place it in the `bin` folder of the app.

    curl https://raw.githubusercontent.com/automine/TA-user-agents/master/bin/fetch_latest.sh -o bin/fetch_latest.sh
    chmod +x bin/fetch_latest.sh

To update user agent string data run the `bin/refresh_latest.sh` script.  This will update not only the browser strings information (`regexes.yaml`), but the python module as well.  If you'd like to run this on a regular basis, consider setting this up as a cron job, or as a scripted input at an appropriate interval.

For example, to refresh every Monday at 4AM, add the following `inputs.conf` entry:

    [script://./bin/fetch_latest.sh local]
    interval = 0 4 * * 1
    index = _internal

Note:  This script on works on Unix, requires `git`, and will clobber any local customizations to `regexes.yaml`.

While this script would ideally be included in the app, this is not possible due to Splunk Cloud packaging standards.  According to the [Vetting apps and add-ons for Splunk Cloud][cloud-packaging] an app "[may] not provide automatic update features for scripts, executables, or libraries."  Sorry.


## Support
Support is on a best-effort basis. Need help? Use the Splunk community resources! I can be found on many of them:

* [Splunk Answers](https://answers.splunk.com/)
* [#splunk on Efnet IRC](https://wiki.splunk.com/Community:IRC)
* [Splunk Slack channel](http://splunk402.com/chat/)

The git repo for this app is located [here](https://github.com/automine/TA-user-agents).

## Credits
This TA uses a Python module from:

https://github.com/ua-parser

Icons made by [Freepik](http://www.freepik.com) from [Flaticon](http://www.flaticon.com) is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/)

## Change log

### v 1.7.1
* Removed the `fetch_latest.sh` from the app to comply with Splunk Cloud packaging standards.  Download link provided above.

### v 1.7.0
* Created script to automate the upgrading of the latest versions of ua-parser
* Imported the latest version of Python libraries ua-parser and PyYAML

### v 1.6
* Updated to the latest version of the ua-parser
* Changed URL for the ua-parser to the new project page
* Added app icons

### v 1.5
Initial release

[cloud-packaging]: http://dev.splunk.com/view/app-cert/SP-CAAAE85
[fetch_latest]: https://github.com/automine/TA-user-agents/blob/master/bin/fetch_latest.sh
