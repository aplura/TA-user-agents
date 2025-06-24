# Updating the Python modules and parsers
Due to Cloud Vetting, the `fetch_latest` script is no longer an executable. 
It is still included, but needs renamed from `fetch_latest.sample` to `fetch_latest.sh`, then properly executed in the environment.


To fetch the latest user agent matching rules run the `bin/refresh_latest.sh` script.  This will update not only the browser strings information (`regexes.yaml`), but the python module as well.  If you'd like to run this on a regular basis, consider setting this up as a cron job, or as a scripted input at an appropriate interval.

For example, to refresh every Monday at 4AM, add the following `inputs.conf` entry:

    [script://./bin/fetch_latest.sh local]
    interval = 0 4 * * 1
    index = _internal

Note:  This script on works on Unix, requires `git`, and will clobber any local customizations to `regexes.yaml`.
