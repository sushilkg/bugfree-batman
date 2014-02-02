#!/usr/bin/python

from datetime import datetime, timedelta
import calendar, os

# list of directory to track error logs into
# directory_to_check = ['./', 'admin/', 'blog/', 'some/other/directory/']
directory_to_check = ['./']

week_ago = datetime.now() - timedelta(days = 7)
week_ago = calendar.timegm(week_ago.utctimetuple())
now = calendar.timegm(datetime.now().utctimetuple())
array = []

for directory in directory_to_check:
	if os.path.isfile(directory+'error_log'): # check if error_log exists	
		log = open( "error_log", "r" )
		array.append('++++++++++++ errors from '+directory+' ++++++++++++ ')
		for line in log:
			error_date = calendar.timegm(datetime.strptime(line[1:20], '%d-%b-%Y %H:%M:%S').utctimetuple())

			# if error_date is more than week
			if(now - error_date) > (now - week_ago):
				continue
			elif array.count(line[39:]) == 0: # if no similar error has been recorded
				array.append(line[1:21]) # save this date
				array.append(line[39:]) # save this new error
		log.close()

new_errors = file('new_errors.log', "w+")
for item in array:
	print >> new_errors, item
new_errors.close()

import errors_send
