
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from callVehic import *
from vehicleDatabase import *

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cors = CORS(app)


# Update the database with new entries 
@app.route("/getData", methods = ["POST"])
def getData():
    if(request.method == "POST"):
        # JSON Format from frontend
        requestData = request.get_json()

        # TODO: Need to establish way to save data to a specific vehicle database (currently only to testing)

        # Initialize the vehicle datapoints  
        altitude = requestData['altitude']
        battery = requestData['battery']

        # Update the vehicle dictonary with given values 
        requestedVehicle = saveVehicleValues.new_battery(battery)
        requestedVehicle = saveVehicleValues.new_altitude(altitude)
       
        # Save the vehicle dictonary into SQLite Database
        vehicleDatabase.saveData(requestedVehicle)

        # TEST: show that the vehicle dictionary has been saved correctly
        return '''The value is: {}'''.format(requestedVehicle)

@app.route("/postData", methods = ["POST"])
def postData():
    if(request.method == "POST"):
        # JSON Format from frontend
        requestData = request.get_json()

        # Initialize the requested vehicle_name
        vehicle_name = requestData['vehicle_name']
        
        # Query the database for the requested vehicle & save into dictonary
        requestedVehicle = vehicleDatabase.getData(vehicle_name)

        # Send JSON Object back to frontend
        return jsonify(requestedVehicle)


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")