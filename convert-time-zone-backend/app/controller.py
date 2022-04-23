from select import select
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
    selectedTimeZoneName = ''
    for x in data:
        if(x['id'] == selectedTimeZone):
            selectedTimeZoneName= x['name'] 
    currentDateAndTime = datetime.now(pytz.timezone(selectedTimeZoneName))
    return currentDateAndTime

def getSelectedTimeZone(currentTimeZoneVal):
    data = d['timeZones']
    selectedTimeZoneName = ''
    for x in data:
        if(x['id'] == currentTimeZoneVal):
            selectedTimeZoneName= x['name'] 
    return selectedTimeZoneName