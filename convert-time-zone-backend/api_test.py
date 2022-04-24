import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:8080"
    ALL_TIMEZONE_URL = "{}/api/getalltimezones".format(API_URL)
    GET_CURRENT_ZONE = "{}/api/getcurrentzonetime".format(API_URL)

    CURRENT_DATE_TIME = {
        "selectTimeZone": "1"
    } 

    #test the get all time zones API sends a status code 200 (passed)
    def test_1_get_all_timeZones_statusCode(self):
        r = requests.get(ApiTest.ALL_TIMEZONE_URL)
        self.assertEqual(r.status_code, 200)

    #test the getAllTimeZones [GET] API length(only one has so this is passed)
    def test_2_get_all_timeZones_response_length(self):
        r = requests.get(ApiTest.ALL_TIMEZONE_URL)
        self.assertEqual(len(r.json()),1)

    #test the getCurrentTime [POST] API to submit a selectTimeZone (passed)
    def test_3_get_current_Time_submit(self):
        r = requests.post(ApiTest.GET_CURRENT_ZONE, json = ApiTest.CURRENT_DATE_TIME)
        self.assertEqual(r.status_code, 200)
    