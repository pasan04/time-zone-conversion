from select import select
from time import time
import pytz
from datetime import datetime
import json

with open('timezone.json') as f:
    d = json.load(f)

#Get all the timezones defined in json file
def getAllTimeZones():
    return d

#Get the current time
def getCurrentTime(selectedTimeZone):
    data = d['timeZones']
    selectedTimeZoneName = ''
    for x in data:
        if(x['id'] == selectedTimeZone):
            selectedTimeZoneName= x['name'] 
    currentDateAndTime = datetime.now(pytz.timezone(selectedTimeZoneName))
    return currentDateAndTime

#Get the selected time zone which sends the name of it extract from json
def getSelectedTimeZone(currentTimeZoneVal):
    data = d['timeZones']
    selectedTimeZoneName = ''
    for x in data:
        if(x['id'] == currentTimeZoneVal):
            selectedTimeZoneName= x['name'] 
    return selectedTimeZoneName