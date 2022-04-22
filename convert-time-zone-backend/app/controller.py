from time import time
import pytz
from datetime import datetime
import json

with open('timezone.json') as f:
    d = json.load(f)

def getAllTimeZones():
    return d

def getCurrentTime(currentTime,timeZone):
    currentTimeZone = timeZone
    data = d['timeZones']
    for x in data:
        if(x['id'] == currentTimeZone):
            selectedTimeZone = x['name']
    datetimenow = currentTime
    time1 = datetime.now(pytz.timezone('US/Eastern'))
    time2 = datetime.now(pytz.timezone('Europe/London'))
    print(time1)
    print(time2)
    # for tz in pytz.all_timezones:
    #     print(tz)