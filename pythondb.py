# Import the tinydb library 
from tinydb import TinyDB, Query
from ToVehicle import *

# https://tinydb.readthedocs.io/en/latest/getting-started.html
# https://github.com/msiemens/tinydb/

# Grab the file 
db = TinyDB('db.json')

stage_name = "Stage "
stage_counter = 0
stage = stage_name + str(stage_counter)
altitude_update = 9



# JSON array is created
data = {'Altitude': altitude_update , 'Battery': 1}

#{{'Altitude': float, 'Battery': float, 'Current Stage': int, 'GeoFence Compliant': boolean, 
#  'Latitude': float, 'Longitude': float, 'Pitch': float, 'Propulsion': float, 'Roll': float, 
#  'Sensors OK': boolean, 'Speed': float, 'Stage Completed': boolean, 'Status': int, 'Yaw': float, 
#  'Time_since_last packet': int, 'Last_packet_time': int}}

example = ToVehicle.data()

for ex in example:
    db.insert(ex)


# Added into the database
#db.insert(example)

query = Query()
print(db.search(query.Altitude == 9))
#print(db.all())

# Manually adds a json array 
#db.insert({'int': 1, 'char': 'b'})

#db.update 

# Clears the document 
#db.truncate()


print(db.all())