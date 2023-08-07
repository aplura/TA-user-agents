# PAVO TA User Agents Documentation

Provides an external Python lookup that parses User Agents strings.

## About PAVO TA User Agents

|                            |                                 |
|----------------------------|---------------------------------|
| Author                     | Aplura, LLC                     |
| App Version                | 1.7.8                           |
| App Build                  | 24                              |
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

## Event Generator

PAVO TA User Agents does not include an event generator.

## Acceleration

- Summary Indexing: No

- Data Model Acceleration: No

- Report Acceleration: No

# Prerequisites, Installation, and Configuration

Because this App runs on Splunk Enterprise, all the [Splunk Enterprise system requirements](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) apply.

## Installation and Configuration

### Download

## Installation Process Overview

- Install the extension.

### Deploy to single server instance

Follow these steps to install the app in a single server instance of Splunk Enterprise:

- Deploy as you would any App, and restart Splunk.

- Configure.

### Deploy to Splunk Cloud

- Have your Splunk Cloud Support handle this installation.

### Deploy to a Distributed Environment

- For each Search Head in the environment, deploy a copy of the App.

# Support and resources

## Questions and answers

Access questions and answers specific to PAVO TA User Agents at <https://community.splunk.com>. Be sure to tag your question with the App.

## Support

- Support Email: <customersupport@aplura.com>

- Support Offered: Splunk Answers, Email

### Logging

Copy the \`\`log.cfg\`\` file from \`\`default\`\` to \`\`local\`\` and change the settings as needed.

### Diagnostics Generation

If a support representative asks for it, a support diagnostic file can be generated. Use the following command to generate the file. Send the resulting file to support.

\`\`\$SPLUNK_HOME/bin/splunk diag --collect=app:TA-user-agents\`\`

## Known Issues

Version 1.7.8 of PAVO TA User Agents has the following known issues:

- None

## Release notes

### Version 1.7.7

- Improvement

  - Removed Python that was flagged by Upgrade Readiness App.

### Version 1.7.5

- Improvement

  - Modified Script for Splunk Cloud compatability.

### Version 1.7.4

- Improvement

  - Updated for Python 3 and Splunk 8 compatability

# Third Party Notices

Version 1.7.8 of PAVO TA User Agents incorporates the following Third-party software or third-party services.

- ua_parser

- pyyaml
