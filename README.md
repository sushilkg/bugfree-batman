About

The script will help you get latest (PHP) errors occured within last week as recorded in different error_logs file. It is useful for old php sites where probability of bugs are high.

Installation & Use

* Copy errors_latest.py and errors_send.py to root directory.
* Modify errors_latest.py to include directories you want error_logs to be scanned from.
* Modify errors_send.py to recieve concatinated errors in your gmail.
* Run errors_latest.py.

To get this done automatically every week, please use crontab. Refer to http://stackoverflow.com/questions/4460262/running-a-python-script-with-cron.

Note: No bashing please, I just started to learn Python. :)
