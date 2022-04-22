from time import time
import pytz
from datetime import datetime
import json

with open('timezone.json') as f:
    d = json.load(f)

def getAllTimeZones():
    return d

def getCurrentTime(currentTimeZone,selectedTimeZone):
    data = d['timeZones']
    for x in data:
        if(x['id'] == currentTimeZone):
            x['name'] = selectedTimeZone
    time1 = datetime.now(pytz.timezone('US/Eastern'))
    print(time1)
    # for tz in pytz.all_timezones:
    #     print(tz)