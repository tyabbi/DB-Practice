# How the json format is updating with real variables 
from abc import ABC
from vehicleDataFormat import *

# https://docs.python.org/3/library/abc.html


class updateVehicle():
    vehicleEntry = vehicleDataFormat.dataFormat()
    def __init__(self, vehicleEntry):
        #self.vehicleName =  vehicleEntry
        #self._altitude = self.vehicleName['Altitude']
        #self._altitude = self.vehicleEntry['Altitude']
        self._altitude = altitude
    

    def set_altitude(self, altitude):
        if(type(altitude)) == float:
            self._altitude = altitude
        
    def get_altitude(self):
        return self._altitude

    vehicleEntry = vehicleDataFormat.dataFormat()
    def set_altitude(altitude):    
        vehicleEntry['Altitude'] = altitude
        

        