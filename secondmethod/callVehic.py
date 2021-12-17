from vehicDataFormat import *

# Create vehicle dictionary from vehicleDataFormat.py
vehicleEntry = vehicleDataFormat.dataFormat()

class saveVehicleValues():

    # TODO: add the methods for all datapoints
    
    # Methods to save the new datapoints into the vehicle dictionary
    def new_altitude(altitude):
        vehicleDataFormat.set_altitude(vehicleEntry, altitude)
        return vehicleEntry 

    # Altitude color

    def new_battery(battery):
        vehicleDataFormat.set_battery(vehicleEntry, battery)
        return vehicleEntry
        
    # Battery color 

    def new_currentStage(stage):
        vehicleDataFormat.set_currentStage(vehicleEntry, stage)
        return vehicleEntry    



