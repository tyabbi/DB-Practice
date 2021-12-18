
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from updateVehicle import *
from vehicleDatabase import *

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cors = CORS(app)


# Update the database with new entries 
@app.route("/sendData", methods = ["POST"])
def sendData():
    if(request.method == "POST"):
        # JSON Format from frontend
        requestData = request.get_json()

        # Initialize the requested vehicle name
        vehicleName = requestData['vehicle_name']

        # Initialize the vehicle datapoints  
        altitude = requestData['altitude']
        altitudeColor = requestData ['altitude_color']
        battery = requestData['battery']
        batteryColor = requestData['battery_color']
        

        # Update the vehicle dictionary with given values 
        requestedVehicle = updateVehicle.newAltitude(altitude)
        requestedVehicle = updateVehicle.newAltitudeColor(altitudeColor)
        requestedVehicle = updateVehicle.newBattery(battery)
        requestedVehicle = updateVehicle.newBatteryColor(batteryColor)

       
        # Save the vehicle dictionary into SQLite Database
        vehicleDatabase.saveData(requestedVehicle, vehicleName)

        # TEST: show that the vehicle dictionary has been saved correctly
        return '''The value is: {}'''.format(requestData)

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


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")