from vehicDataFormat import *

#altitude = 8.0

mac = vehicleDataFormat.dataFormat()
class callVehicles():
#vehicleEntry = vehicleDataFormat.dataFormat()
#print(vehicleEntry['Altitude'])
#vehicleEntry['Altitude'] = altitude
#print(vehicleEntry['Altitude'])

#print(vehicleDataFormat.get_altitude(mac))
#vehicleDataFormat.set_altitude(mac, altitude)
#print(vehicleDataFormat.get_altitude(mac))



    def alt(altitude):
        vehicleDataFormat.set_altitude(mac, altitude)
        #print(mac)
        return mac 
    def bat(battery):
        vehicleDataFormat.set_battery(mac, battery)
        return mac


