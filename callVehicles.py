# Calling the vehicle.py for each vehicle 


from vehicleDataFormat import *

altitude = 8.0

mac = vehicleDataFormat.dataFormat()
class callVehicles():
#vehicleEntry = vehicleDataFormat.dataFormat()
#print(vehicleEntry['Altitude'])
#vehicleEntry['Altitude'] = altitude
#print(vehicleEntry['Altitude'])

#print(vehicleDataFormat.get_altitude(mac))
#vehicleDataFormat.set_altitude(mac, altitude)
#print(vehicleDataFormat.get_altitude(mac))

#print(mac)

    def macVehicle():
        vehicleDataFormat.set_altitude(mac, altitude)
        #print(mac)

        return mac 