# Import the tinydb library 
from tinydb import TinyDB, Query
from ToVehicle import *


# https://tinydb.readthedocs.io/en/latest/getting-started.html
# https://github.com/msiemens/tinydb/

# Grab the file 
db = TinyDB('db.json')
TinyDB.default_table_name = 'table'

stage_name = "Stage "
stage_counter = 0
stage = stage_name + str(stage_counter)
altitude_update = 9
altitude_value = 2

# JSON array is created
data = {'Altitude': altitude_update , 'Battery': 1}

#{{'Altitude': float, 'Battery': float, 'Current Stage': int, 'GeoFence Compliant': boolean, 
#  'Latitude': float, 'Longitude': float, 'Pitch': float, 'Propulsion': float, 'Roll': float, 
#  'Sensors OK': boolean, 'Speed': float, 'Stage Completed': boolean, 'Status': int, 'Yaw': float, 
#  'Time_since_last packet': int, 'Last_packet_time': int}}

example = ToVehicle.data1()


table = db.table('vehicle_1')

table1 = db.table('vehicle_2')

table.insert(data)
table1.insert(example)

#for ex in example:
#    db.insert(ex)

# Added into the database
#db.insert(example)

query = Query()
print(table1.search(query.Altitude == 0.0))
#print(db.all())

# Manually adds a json array 
#db.insert({'int': 1, 'char': 'b'})

#db.update 

# Clears the document 
#db.truncate()


#el = db.get(query.Altitude == 0)
#print(doc_id)