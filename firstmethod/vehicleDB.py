# Putting the json format into the database 

# Import the TinyDB, vehicleDataFormat, json libraries 
from tinydb import TinyDB, Query
#from callVehicles import macVehicle
from vehicleDataFormat import *
from callVehicles import *
import json

# TinyDB documentation/help links:
# https://tinydb.readthedocs.io/en/latest/getting-started.html
# https://tinydb.readthedocs.io/en/latest/usage.html#
# https://github.com/msiemens/tinydb/

# Grab the file 
db = TinyDB('db.json')

# Name the table to a different name
TinyDB.default_table_name = 'table'

# Mock up variable change 
altitude_update = 50
altitude_color = "Green"
battery = 60
battery_color = "Yellow"

# Mock up JSON array is created
data = {'Altitude': altitude_update , 'Atitude_Color': altitude_color, 'Battery': battery, 'Battery_Color': battery_color}

# Call the jsonFormat for the vehicle
uavEntry = vehicleDataFormat.dataFormat()
ugvEntry = vehicleDataFormat.dataFormat()

#print(ugvEntry['Altitude'])
macVehicle1 = callVehicles.macVehicle()
# Define the name of each document (each vehicle)
uav_table = db.table('UAV_Entries')
ugv_table = db.table('UGV_Entries')
vehicle = db.table('vehicle')

#vehicle.insert(data)

# How to add data to each document
#uav_table.insert(macVehicle1)
#ugv_table.insert(ugvEntry)

# Call the query class
query = Query()

# How to make a query for an attribute
print(json.dumps(vehicle.all(), indent = 2))
uavValues = uav_table.search(query.Altitude == 8.0)
#print(uavValues)
# Convert list to JSON string and print (formatting choice)
#print(json.dumps(vehicle, indent = 2))

# Print out the list (different format choice)
#for x in range(len(values)):
#    print (values[x])

# Print all the documents 
#print(db.all())

# Print a specific table 
#print(uav_table.all())

# Clears the database
#db.truncate()