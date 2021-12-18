from vehicleDataFormat import *
from vehicleDatabase import *

# testingUpdate.py is for testing dictionary updating 

# TODO: check if this method is valid 

# Create vehicle dictionary from vehicleDataFormat.py
vehicleEntry = vehicleDataFormat.dataFormat()

# New Entry
newData = {"vehicle_name": "testing",
"altitude": 100.0,
"altitude_color": "Red",
"battery": 15.0,
"battery_color": "Blue"}

# Initialize requested vehicle 
vehicleName = newData['vehicle_name']

# Updates dictionary format with new entry
vehicleEntry.update(newData)
# vehicle_name is not required
vehicleEntry.pop('vehicle_name')

# Save to database
#vehicleDatabase.saveData(vehicleEntry, vehicleName)

