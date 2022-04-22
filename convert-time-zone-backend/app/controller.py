from pytz import timezone
from datetime import datetime
import json

with open('timezone.json') as f:
    d = json.load(f)

def getAllTimeZones():
    return d

def getCurrentTime():
    time_format = '%d-%m-%Y %H:%S'
    datetimenow = datetime.now()
    print(datetimenow)