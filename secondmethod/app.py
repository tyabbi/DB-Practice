
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from callVehic import *
from vehicleDatabase import *

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cors = CORS(app)

@app.route("/get_data", methods = ["POST"])
def get_data():
    if(request.method == "POST"):
        # JSON Format from frontend
        request_data = request.get_json()
        altitude = request_data['altitude']
        battery = request_data['battery']

        macVehicle = callVehicles.new_battery(battery)
        macVehicle = callVehicles.new_altitude(altitude)
       
        vehicleDatabase.saveData(macVehicle)

        return '''The value is: {}'''.format(macVehicle)
    
    # GET REQUEST
    return "Hello World :))"

@app.route("/post_data", methods = ["POST"])
def post_data():
    if(request.method == "POST"):
        # JSON Format from frontend
        request_data = request.get_json()
        vehicle_name = request_data['vehicle_name']
        
        macVehicle = vehicleDatabase.getData(vehicle_name)
        #return '''The value is: {}'''.format(macVehicle)

        #print(macVehicle)
        return jsonify(macVehicle)
    
    # GET REQUEST
    return "Hello World :))"


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")