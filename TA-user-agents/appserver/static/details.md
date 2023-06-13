# PAVO TA User Agents Documentation

Provides an external Python lookup that parses User Agents strings.

## About PAVO TA User Agents

|                            |                                 |
|----------------------------|---------------------------------|
| Author                     | Aplura, LLC                     |
| App Version                | 1.7.7                           |
| App Build                  | 21                              |
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
