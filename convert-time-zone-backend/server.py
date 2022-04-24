from time import time
from flask import Flask, jsonify, request,json
from flask_cors import CORS
from flask_restful import Api, Resource
from pyparsing import null_debug_action
import app.controller as controller

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class PostResource(Resource):
    def get(self):
        return {'data' : 'Get Request'}

#Get all the timezones api
@app.route('/api/getalltimezones', methods =['GET'])
def getAllTimeZones():
    return jsonify(controller.getAllTimeZones())

#get the current time api
@app.route('/api/getcurrentzonetime',methods = ['POST'])
def getCurrentTime():
    content = request.get_json(force=True)
    selectedTimeZone = content['selectTimeZone']
    currentDateAndTime = controller.getCurrentTime(selectedTimeZone)
    selectedTimeZoneName = controller.getSelectedTimeZone(selectedTimeZone)
    convertedDate = currentDateAndTime.strftime("%a, %b %d, %Y")
    convertedTime = currentDateAndTime.strftime("%I:%M:%S %p")
    convertedDateTime = {
        "convertedTime": convertedTime,
        "convertedDate": convertedDate,
        "selectedTimeZone": selectedTimeZoneName
    }
    return jsonify(convertedDateTime)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
