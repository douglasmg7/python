#!/usr/bin/python
from datetime import datetime, date, time, timedelta
dt = datetime(2024,6,15,13,3,1)
print(f'datetime: {dt}')
print(f'datetime: {dt.strftime("%y/%m/%d %H:%M:%S")}')
print(f'day: {dt.day}')

print(f'date: {dt.date()}')
print(f'time: {dt.time()}')
dts = datetime.strptime("20091031", "%Y%m%d")
print(f'parsed: {dts}')

# Replace
dts = dts.replace(minute=30, second=59)
print(f'replaced: {dts}')

# Time delta
delta = dt - dts 
print(f'dt: {dt}')
print(f'dts: {dts}')
print(f'delta: {delta}')
new_delta = timedelta(days=3)
print(f'new delta: {new_delta}')

# Shift
new_date = dts + new_delta
print(f'shift: {new_date}')