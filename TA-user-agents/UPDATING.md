# Updating the Python modules and parsers
In 1.7.2, @lowell80 was nice enough to contribute a script for updating the
Python modules this TA uses.
Unfortunately, there were commands in this script which caused the app to fail
Splunk Cloud vetting, so that it cannot be installed by Cloud customers.

To solve this, we have repackaged the app without the script, and resubmitted it
for vetting.

As such, the `fetch_latest` script is no longer included in the download from
Splunkbase. However, the script is still available for download from the
Github repo:

https://github.com/automine/TA-user-agents/blob/master/bin/fetch_latest.sh

To fetch the latest user agent matching rules run the `bin/refresh_latest.sh` script.  This will update not only the browser strings information (`regexes.yaml`), but the python module as well.  If you'd like to run this on a regular basis, consider setting this up as a cron job, or as a scripted input at an appropriate interval.

For example, to refresh every Monday at 4AM, add the following `inputs.conf` entry:

    [script://./bin/fetch_latest.sh local]
    interval = 0 4 * * 1
    index = _internal

Note:  This script on works on Unix, requires `git`, and will clobber any local customizations to `regexes.yaml`.
