# Calling the vehicle.py for each vehicle 

from updateVehicle import *
from vehicleDataFormat import *

altitude = 3.0

mac = vehicleDataFormat.dataFormat()
#updateVehicle.set_altitude(mac, 0.0)
#print(updateVehicle.get_altitude(mac))
#print(mac['Altitude'])]

class callVehicles(): 
    #vehicleEntry = vehicleDataFormat.dataFormat()
    def set_altitude(altitude):    
        vehicleEntry = vehicleDataFormat.dataFormat()
        vehicleEntry['Altitude'] = altitude

callVehicles.set_altitude(mac, 3.0)
print(mac['Altitude'])
