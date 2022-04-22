from flask import Flask, jsonify, request,json
from flask_cors import CORS
from flask_restful import Api, Resource
from pyparsing import null_debug_action
import app.controller as controller

app = Flask(__name__)
CORS(app)
api = Api(app)


#Get all the timezones
@app.route('/api/getalltimezones', methods =['GET'])
def getAllTimeZones():  
    return jsonify(controller.getAllTimeZones())

#get the current time
@app.route('/api/getcurrenttime',methods = ['GET'])
def getCurrentTime():
    localTime = controller.getCurrentTime()
    return 'ppp'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
