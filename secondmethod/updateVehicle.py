import json
from vehicleDataFormat import *
from datetime import datetime
from vehicleDatabase import *
from generalStage import *

# updateVehicle.py handles saving new mission entry datapoints to the data format

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
    # def newBatteryColor(batteryColor):
    #     vehicleDataFormat.setBatteryColor(vehicleEntry, batteryColor)
    #     return vehicleEntry

    def newCurrentStage(stage):
        vehicleDataFormat.setCurrentStage(vehicleEntry, stage)
        return vehicleEntry 

    def newGeofenceCompilant(isCompilant):
        vehicleDataFormat.setGeofenceCompliant(vehicleEntry, isCompilant)
        return vehicleEntry 

    # Geofence Color

    def newLatitude(latitude):
        vehicleDataFormat.setLatitude(vehicleEntry, latitude)
        return vehicleEntry 

    def newLongitude(longitude):
        vehicleDataFormat.setLongitude(vehicleEntry, longitude)
        return vehicleEntry 

    def newPitch(pitch):
        vehicleDataFormat.setPitch(vehicleEntry, pitch)
        return vehicleEntry 

    # Pitch color

    def newPropulsion(propulsion):
        vehicleDataFormat.setPropulsion(vehicleEntry, propulsion)
        return vehicleEntry 
    
    # Propulsion Color

    def newRoll(roll):
        vehicleDataFormat.setRoll(vehicleEntry, roll)
        return vehicleEntry 
    
    # Roll Color

    def newSensorsOk(sensorOk):
        vehicleDataFormat.setSensorsOk(vehicleEntry, sensorOk)
        return vehicleEntry 

    def newSpeed(speed):
        vehicleDataFormat.setSpeed(vehicleEntry, speed)
        return vehicleEntry

    def newStageCompleted(stageComplete):
        vehicleDataFormat.setStageCompleted(vehicleEntry, stageComplete)
        return vehicleEntry

    def newStatus(status):
        vehicleDataFormat.setStatus(vehicleEntry, status)
        return vehicleEntry
    
    def newYaw(yaw):
        vehicleDataFormat.setYaw(vehicleEntry, yaw)
        return vehicleEntry

    def newTimeSinceLastPacket(timeSinceLastPacket):
        vehicleDataFormat.setTimeSinceLastPacket(vehicleEntry, timeSinceLastPacket)
        return vehicleEntry

    def newLastPacketTime(lastPacketTime):
        vehicleDataFormat.setLastPacketTime(vehicleEntry, lastPacketTime)
        return vehicleEntry

    def newTime(time):
        vehicleDataFormat.setTime(vehicleEntry, time)
        return vehicleEntry

    def newStageName(stageName):
        vehicleDataFormat.setStageName(vehicleEntry, stageName)
        return vehicleEntry

    def newMode(mode):
        vehicleDataFormat.setMode(vehicleEntry, mode)
        return vehicleEntry

# ask matthew about this 
# Autonomous
# Manual

# Adding new entries to database
class updateDatabase():    
    vehicleDatabase()
    def newEntries():
        updateVehicle()
        vehicleFormat = {
                'vehicle_name': 'MEA',
                'altitude': 100.0,
                'altitude_color': 'None',
                'battery': 23.0,
                #'battery_color': 'None',
                'current_stage': 1,
                'geofence_compliant': False,
                'geofence_compliant_color': 'None',
                'latitude': 33.9344055,
                'longitude': -117.6306099,
                'mode':'Manual',
                'pitch': 87.0,
                'pitch_color': 'None',
                'propulsion': True,
                'propulsion_color': 'None',
                'roll': 20.0,
                'roll_color': 'None',
                'sensors_ok': True,
                'speed': 49.0,
                'stage_completed': True,
                'status': 5,
                'yaw': 12.0,
                'time_since_last_packet': 78,
                'last_packet_time': 100,
                # need to add this to comms 
                'time': '2022-01-01 00:00:00',
                'stage_name': 'None'
        }

        # Initialize the requested vehicle name
        vehicleName = vehicleFormat['vehicle_name']

        # Initialize the vehicle datapoints  
        altitude = vehicleFormat['altitude']
        battery = vehicleFormat['battery']
        currentStage = vehicleFormat['current_stage']
        geofenceCompilant = vehicleFormat['geofence_compliant']
        latitude = vehicleFormat['latitude']
        longitude = vehicleFormat['longitude']
        pitch = vehicleFormat['pitch']
        propulsion = vehicleFormat['propulsion']
        roll = vehicleFormat['roll']
        sensorsOk = vehicleFormat['sensors_ok']
        speed = vehicleFormat['speed']
        stageComplete = vehicleFormat['stage_completed']
        status = vehicleFormat['status']
        yaw = vehicleFormat['yaw']
        timeSinceLastPacket = vehicleFormat['time_since_last_packet']
        lastPacketTime = vehicleFormat['last_packet_time']
        time = vehicleFormat['time']
        mode = vehicleFormat['mode']

        # Gets the stage name of the sent stage id 
        stageName = updateStage.updateStageName(currentStage)
        
        # Update the vehicle dictionary with given values 
        requestedVehicle = updateVehicle.newAltitude(altitude)
        requestedVehicle = updateVehicle.newBattery(battery)
        requestedVehicle = updateVehicle.newCurrentStage(currentStage)
        requestedVehicle = updateVehicle.newGeofenceCompilant(geofenceCompilant)
        requestedVehicle = updateVehicle.newLatitude(latitude)
        requestedVehicle = updateVehicle.newLongitude(longitude)
        requestedVehicle = updateVehicle.newPitch(pitch)
        requestedVehicle = updateVehicle.newPropulsion(propulsion)
        requestedVehicle = updateVehicle.newRoll(roll)
        requestedVehicle = updateVehicle.newSensorsOk(sensorsOk)
        requestedVehicle = updateVehicle.newSpeed(speed)
        requestedVehicle = updateVehicle.newStageCompleted(stageComplete)
        requestedVehicle = updateVehicle.newStatus(status)
        requestedVehicle = updateVehicle.newYaw(yaw)
        requestedVehicle = updateVehicle.newTimeSinceLastPacket(timeSinceLastPacket)
        requestedVehicle = updateVehicle.newLastPacketTime(lastPacketTime)
        requestedVehicle = updateVehicle.newTime(time)
        requestedVehicle = updateVehicle.newStageName(stageName)
        requestedVehicle = updateVehicle.newMode(mode)
    
        vehicleDatabase.saveData(requestedVehicle, vehicleName)

# TESTING PURPOSE (add new entries to the database)
updateDatabase.newEntries()