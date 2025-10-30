# PAVO TA User Agents Documentation

Provides an external Python lookup that parses User Agents strings.

## About PAVO TA User Agents

|                            |                                 |
|----------------------------|---------------------------------|
| Author                     | Aplura, LLC                     |
| App Version                | 1.7.10                          |
| App Build                  | 47                              |
| Release Date               | 2025-10-30                      |
| Creates an index           | False                           |
| Implements summarization   | No                              |
| Summary Indexing           | False                           |
| Data Model Acceleration    | If Enabled                      |
| Report Acceleration        | False                           |
| Splunk Enterprise versions |                                 |
| Platforms                  | Splunk Enterprise, Splunk Cloud |

## Scripts and binaries

This App provides the following scripts:

|                     |                                                                           |
|---------------------|---------------------------------------------------------------------------|
| Diag.py             | For use with the diag command.                                            |
| fetch_latest.sample | For grabbing the most recent versions of the libraries.                   |
| user_agents.py      | This is the lookup command python to parse the user agent.                |
| Utilities.py        | This is a supporting python script for use with logging, and other needs. |
| version.py          | This contains the version of the package.                                 |
| app_properties.py   | This contains app properties.                                             |

<div class="note">

`fetch_latest.sample` is a bash script that would need to be renamed and have +x added to it in order to be a valid script. This script updates the libraries for on-prem installations.

</div>

## Lookups

PAVO TA User Agents contains the following lookup files.

- None

## Usage

While PAVO TA User Agents does not include lookup files, it is a dynamic lookup.

\`\`\` \<SPL\> \| lookup user_agents http_user_agent AS \<user agent field\> \`\`\`

## Event Generator

PAVO TA User Agents does not include an event generator.

## Acceleration

- Summary Indexing: No

- Data Model Acceleration: No

- Report Acceleration: No

# Update latest data

If the need for pulling updated libraries before a re-release of this app, use the following script. This script should be included in `bin/` but cannot be included within the app itself due to Splunk AppInspect Restrictions.

``` bash
#!/bin/bash
# This script will pull down the latest python modules from the upstream
# maintainers using git.  This updates not only the regexes.yaml file, but all
# the python code.
#
# This script is indented to be useful to both end-users simply wanting the
# latest User Agent strings as well as the TA maintainer (or anyone else
# storing their Splunk apps in git) periodically refreshing this content.
#
# Even though uap-core is a submodule of uap-python, to always get the latest
# UA parsing configuration, this script pulls both repos independently.  Since
# the submodule isn't initialize, this doesn't result in duplicate work.
#
#   WARNING: Any local customizations to regexes.yaml will be overwritten.
#
# Author:  Lowell Alleman (lowell@kintyre.co)

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
MYNAME=$(basename "${BASH_SOURCE[0]}")
BIN_DIR=$(pwd)
REPOS="$BIN_DIR/repos"

target="$1"
if [[ $target != "local" ]] && [[ $target != "git" ]]
then
    echo "Usage:  $MYNAME  (local|git) " 1>&2
    echo 1>&2
    echo "        Unless you are the TA maintainer, pick 'local'" 1>&2
    exit 1
fi

[[ -x $(command -v git) ]] || { echo "$MYNAME requires 'git'." 1>&2; exit 2; }
[[ -d $REPOS ]] && rm -rf $REPOS
[[ -d $REPOS ]] || mkdir -v "$REPOS"
cd "$REPOS" || exit 1

git clone https://github.com/ua-parser/uap-python.git
git clone https://github.com/ua-parser/uap-core.git

# Confirm that the checkout still contains all the expected folders; If not
# this script will need to be updated to reflect whatever upstream changes.
[[ -d "uap-python/src/ua_parser" ]]  || { echo "Upstream git repo missing 'ua_parser'"; exit 3; }
[[ -f "uap-core/regexes.yaml" ]] || { echo "Upstream git repo missing regexes.yaml'"; exit 3; }

echo "Copying updated python modules into TA-user-agents"
#delete command here incase need to revert, will fail appinspect though -rf "$BIN_DIR/ua_parser" "$BIN_DIR/uap-core"
[[ -d $REPOS ]] || "$BIN_DIR/ua_parser"
[[ -d $REPOS ]] || "$BIN_DIR/uap-core"
# Skip all hidden files
#cp -a "$REPOS"/uap-python/ua_parser/* "$BIN_DIR/ua_parser"
#cp -a "$REPOS"/uap-core/* "$BIN_DIR/uap-core"
cp -R "$REPOS"/uap-python/src/ua_parser/* "$BIN_DIR/ua_parser/"
cp -R "$REPOS"/uap-core/* "$BIN_DIR/uap-core/"
```
