
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from updateVehicle import *
from vehicleDatabase import *
from datetime import datetime

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cors = CORS(app)

# hello this is shaz, this test

# Update the database with new entries 
@app.route("/sendData", methods = ["POST"])
def sendData():
    if(request.method == "POST"):
        # JSON Format from comm
        requestData = request.get_json()

        # Initialize the requested vehicle name
        vehicleName = requestData['vehicle_name']
        #newTime = requestData['time']

        # Initialize the vehicle datapoints  
        altitude = requestData['altitude']
        # altitudeColor = requestData ['altitude_color']
        # battery = requestData['battery']
        # batteryColor = requestData['battery_color']
        currentStage = requestData['current_stage']
        # geofenceCompilant = requestData['geofence_compliant']
        # geofenceCompilantColor = requestData['geofence_compliant_color']
        # latitude = requestData['latitude']
        # longitude = requestData['longitude']
        # pitch = requestData['pitch']
        # pitchColor = requestData['pitch_color']
        # propulsion = requestData['propulsion']
        # roll = requestData['roll']
        # rollColor = requestData['roll_color']
        # sensorsOk = requestData['sensors_ok']
        # speed = requestData['speed']
        # stageComplete = requestData['stage_completed']
        # status = requestData['status']
        # yaw = requestData['yaw']
        # timeSinceLastPacket = requestData['time_since_last_packet']
        # lastPacketTime = requestData['last_packet_time']
        time = requestData['time']
        

        # Update the vehicle dictionary with given values 
        requestedVehicle = updateVehicle.newAltitude(altitude)
        # requestedVehicle = updateVehicle.newAltitudeColor(altitudeColor)
        # requestedVehicle = updateVehicle.newBattery(battery)
        # requestedVehicle = updateVehicle.newBatteryColor(batteryColor)
        requestedVehicle = updateVehicle.newCurrentStage(currentStage)
        # requestedVehicle = updateVehicle.newGeofenceCompilant(geofenceCompilant)
        # requestedVehicle = updateVehicle.newGeofenceCompilantColor(geofenceCompilantColor)
        # requestedVehicle = updateVehicle.newLatitude(latitude)
        # requestedVehicle = updateVehicle.newLongitude(longitude)
        # requestedVehicle = updateVehicle.newPitch(pitch)
        # requestedVehicle = updateVehicle.newPitchColor(pitchColor)
        # requestedVehicle = updateVehicle.newPropulsion(propulsion)
        # requestedVehicle = updateVehicle.newRoll(roll)
        # requestedVehicle = updateVehicle.newRollColor(rollColor)
        # requestedVehicle = updateVehicle.newSensorsOk(sensorsOk)
        # requestedVehicle = updateVehicle.newSpeed(speed)
        # requestedVehicle = updateVehicle.newStageCompleted(stageComplete)
        # requestedVehicle = updateVehicle.newStatus(status)
        # requestedVehicle = updateVehicle.newYaw(yaw)
        # requestedVehicle = updateVehicle.newTimeSinceLastPacket(timeSinceLastPacket)
        # requestedVehicle = updateVehicle.newLastPacketTime(lastPacketTime)
        requestedVehicle = updateVehicle.newTime(time)
       
        # Save the vehicle dictionary into SQLite Database
        vehicleDatabase.saveData(requestedVehicle, vehicleName)
        updateStage.checkTime(time, currentStage)

        # TEST: show that the vehicle dictionary has been saved correctly
        return '''The value is: {}'''.format(requestedVehicle)

@app.route("/postData", methods = ["POST"])
def postData():
    if(request.method == "POST"):
        # JSON Format from frontend
        requestData = request.get_json()

        # Initialize the requested vehicle name
        vehicleName = requestData['vehicle_name']
        
        # Query the database for the requested vehicle & save into dictionary
        requestedVehicle = vehicleDatabase.getData(vehicleName)

        # Send JSON Object back to frontend
        return jsonify(requestedVehicle)

@app.route("/generalStage", methods = ['GET'])
def generalStage():

    jsonFile = open("updateStage.json")
    dataValue = json.load(jsonFile)

    dataFormat = {
        "general_stage": dataValue['general_stage']
    }

    return dataFormat


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")