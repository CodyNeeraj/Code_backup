# Time Conversion from seconds to current 12 hrs format
import datetime,time

seconds = int(input())
mins , secs = divmod(seconds,60)
hrs,mins = divmod(mins,60)
val = "{}:{}:{}".format(hrs,mins,secs)
print("Time in 24 hrs format is = ",val)
d = datetime.datetime.strptime(val, "%H:%M:%S")
# print(d.strftime("%I:%M:%S %p"))
instamt_time = d.strftime("%I:%M:%S")
curr_time = .strftime("%H:%M:%S")
print(curr_time - instamt_time)
