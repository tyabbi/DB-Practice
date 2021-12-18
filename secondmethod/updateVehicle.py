from vehicleDataFormat import *

# Create vehicle dictionary from vehicleDataFormat.py
vehicleEntry = vehicleDataFormat.dataFormat()

class updateVehicle():

    # TODO: add the methods for all datapoints
    
    # Methods to save the new datapoints into the vehicle dictionary
    def newAltitude(altitude):
        vehicleDataFormat.setAltitude(vehicleEntry, altitude)
        return vehicleEntry 

    # Altitude color
    def newAltitudeColor(altitudeColor):
        vehicleDataFormat.setAltitudeColor(vehicleEntry, altitudeColor)
        return vehicleEntry 

    def newBattery(battery):
        vehicleDataFormat.setBattery(vehicleEntry, battery)
        return vehicleEntry
        
    # Battery color 
    def newBatteryColor(batteryColor):
        vehicleDataFormat.setBatteryColor(vehicleEntry, batteryColor)
        return vehicleEntry

    def newCurrentStage(stage):
        vehicleDataFormat.setCurrentStage(vehicleEntry, stage)
        return vehicleEntry 

    def newGeofenceCompilant(isCompilant):
        vehicleDataFormat.setGeofenceCompliant(vehicleEntry, isCompilant)
        return vehicleEntry   




