from vehicDataFormat import *

#altitude = 8.0

mac = vehicleDataFormat.dataFormat()
class callVehicles():

    def new_altitude(altitude):
        vehicleDataFormat.set_altitude(mac, altitude)
        return mac 

    def new_battery(battery):
        vehicleDataFormat.set_battery(mac, battery)
        return mac
        



