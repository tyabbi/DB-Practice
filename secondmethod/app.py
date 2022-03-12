
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from updateVehicle import *
from vehicleDatabase import *
from generalStage import *
from datetime import datetime
from mission import *

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

# {
#     emergencyStop: "MAC"
# }

app = Flask(__name__)
cors = CORS(app)


# hello this is shaz, this test

# # Update the database with new entries 
# @app.route("/sendData", methods = ["POST"])
# def sendData():
#     if(request.method == "POST"):
#         # Object from comm
#         requestData = request.get_json()

#         # Initialize the requested vehicle name
#         vehicleName = requestData['vehicle_name']
#         #newTime = requestData['time']

#         # Initialize the vehicle datapoints  
#         altitude = requestData['altitude']
#         #altitudeColor = requestData ['altitude_color']
#         battery = requestData['battery']
#         #batteryColor = requestData['battery_color']
#         currentStage = requestData['current_stage']
#         geofenceCompilant = requestData['geofence_compliant']
#         bool(geofenceCompilant)
#         #geofenceCompilantColor = requestData['geofence_compliant_color']
#         latitude = requestData['latitude']
#         longitude = requestData['longitude']
#         pitch = requestData['pitch']
#         #pitchColor = requestData['pitch_color']
#         propulsion = requestData['propulsion']
#         roll = requestData['roll']
#         #rollColor = requestData['roll_color']
#         sensorsOk = requestData['sensors_ok']
#         speed = requestData['speed']
#         stageComplete = requestData['stage_completed']
#         status = requestData['status']
#         yaw = requestData['yaw']
#         timeSinceLastPacket = requestData['time_since_last_packet']
#         lastPacketTime = requestData['last_packet_time']
#         time = requestData['time']

#         # Gets the stage name of the sent stage id 
#         stageName = updateStage.updateStageName(currentStage)
        
#         # Update the vehicle dictionary with given values 
#         requestedVehicle = updateVehicle.newAltitude(altitude)
#         #requestedVehicle = updateVehicle.newAltitudeColor(altitudeColor)
#         requestedVehicle = updateVehicle.newBattery(battery)
#         #requestedVehicle = updateVehicle.newBatteryColor(batteryColor)
#         requestedVehicle = updateVehicle.newCurrentStage(currentStage)
#         requestedVehicle = updateVehicle.newGeofenceCompilant(geofenceCompilant)
#         #requestedVehicle = updateVehicle.newGeofenceCompilantColor(geofenceCompilantColor)
#         requestedVehicle = updateVehicle.newLatitude(latitude)
#         requestedVehicle = updateVehicle.newLongitude(longitude)
#         requestedVehicle = updateVehicle.newPitch(pitch)
#         #requestedVehicle = updateVehicle.newPitchColor(pitchColor)
#         requestedVehicle = updateVehicle.newPropulsion(propulsion)
#         requestedVehicle = updateVehicle.newRoll(roll)
#         #requestedVehicle = updateVehicle.newRollColor(rollColor)
#         requestedVehicle = updateVehicle.newSensorsOk(sensorsOk)
#         requestedVehicle = updateVehicle.newSpeed(speed)
#         requestedVehicle = updateVehicle.newStageCompleted(stageComplete)
#         requestedVehicle = updateVehicle.newStatus(status)
#         requestedVehicle = updateVehicle.newYaw(yaw)
#         requestedVehicle = updateVehicle.newTimeSinceLastPacket(timeSinceLastPacket)
#         requestedVehicle = updateVehicle.newLastPacketTime(lastPacketTime)
#         requestedVehicle = updateVehicle.newTime(time)
#         requestedVehicle = updateVehicle.newStageName(stageName)
        
#         # Save the vehicle dictionary into SQLite Database
#         vehicleDatabase.saveData(requestedVehicle, vehicleName)
        

#         # TEST: show that the vehicle dictionary has been saved correctly
#         return geofenceCompilant
#         #return '''The value is: {}'''.format(requestedVehicle)

# Sends back the latest entry from requested vehicle
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

# Compares new request's stage/time to updateStage.json
@app.route("/updateGeneralStage", methods = ['POST'])
def updateGeneralStage():
    if(request.method == "POST"):

        now = datetime.now()
        # Object from frontened
        requestData = request.get_json()

        #print(now)
        #print(requestData)
        updateStage.updateTime(requestData, now)

    return 'Update Complete'

# Sends information from updateStage.json
@app.route("/getGeneralStage", methods = ['GET'])
def getGeneralStage():

    # opens updateStage.json
    jsonFile = open("updateStage.json")
    dataValue = json.load(jsonFile)

    # Saves the information needed to display general stage
    dataFormat = {
        "id": dataValue['general_stage'],
        "vehicle": dataValue['vehicle'],
        "name": dataValue['stage_name']
    }

    return dataFormat

# Saves the new mission entry into newMission.json
@app.route("/createNewMission", methods = ['POST'])
def createNewMission():
    if(request.method == "POST"):

        # Object from frontend
        requestData = request.get_json()

        # Sends the new mission to be saved
        Mission.createMission(requestData)

    return 'Created New Mission'

# Sends back the saved mission from newMission.json
@app.route("/getNewMission", methods = ['GET'])
def getnewMission():
    if(request.method == "GET"):

        # Opens the saved mission entry from the JSON File and saves it into a variable 
        jsonFile = open("newMission.json")
        dataValue = json.load(jsonFile)

    return dataValue

# {
#     "vehicle_name": "testing",
#     "altitude": 54.98, 
#     "current_stage": 1,
#     "time": "2022-01-21 07:15:00"
# }

# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")