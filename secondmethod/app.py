
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from callVehic import *
from vehicleDatabase import *

# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cors = CORS(app)

@app.route("/get_data", methods = ["POST"])
def get_data():
    if(request.method == "POST"):
        request_data = request.get_json()
        altitude = request_data['altitude']
        battery = request_data['battery']

        macVehicle = callVehicles.bat(battery)
        macVehicle = callVehicles.alt(altitude)
       
        
        vehicleDatabase.saveData(macVehicle)

        return '''The value is: {}'''.format(macVehicle)
    
    # GET REQUEST
    return "Hello World :))"


# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")