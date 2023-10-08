# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> time module

import time

print(time.ctime(0))  # reference point (epic)
print(time.ctime(1000000))

print(time.time())
print(time.ctime(time.time()))  # current time (epic)


time_object = time.localtime()
print(time_object)

time_object = time.gmtime()
print(time_object)

local_time = time.strftime('%B %d %Y %H:%M:%S', time_object)
print(local_time)

time_string = '20 April, 2020'
time_object = time.strptime(time_string, '%d %B, %Y')
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)  # year, month, hours, min, sec, day of the week, day of the year, dst
time_str = time.asctime(time_tuple)
print(time_str)

time_str = time.mktime(time_tuple)
print(time_str)
