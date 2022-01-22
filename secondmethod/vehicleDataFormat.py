# the format for the packet inputs (standard)
class vehicleDataFormat():
    
    # Used for setter and getter methods
    def __init__(self):
        self.vehicleFormat = {
            'altitude': 0.0,
            'altitude_color': 'None',
            'battery': 0.0,
            'battery_color': 'None',
            'current_stage': 0,
            'geofence_compliant': False,
            'geofence_compliant_color': 'None',
            'latitude': 0.0,
            'longitude': 0.0,
            'pitch': 0.0,
            'pitch_color': 'None',
            'propulsion': False,
            'propulsion_color': 'None',
            'roll': 0.0,
            'roll_color': 'None',
            'sensors_ok': False,
            'speed': 0.0,
            'stage_completed': False,
            'status': 0,
            'yaw': 0.0,
            'time_since_last_packet': 0,
            'last_packet_time': 0,
            'time': "2022-01-01 00:00:00",
            'stage_name': 'None'
        }


    def dataFormat():
        vehicleFormat = {
            'altitude': 0.0,
            'altitude_color': 'None',
            'battery': 0.0,
            'battery_color': 'None',
            'current_stage': 0,
            'geofence_compliant': False,
            'geofence_compliant_color': 'None',
            'latitude': 0.0,
            'longitude': 0.0,
            'pitch': 0.0,
            'pitch_color': 'None',
            'propulsion': False,
            'propulsion_color': 'None',
            'roll': 0.0,
            'roll_color': 'None',
            'sensors_ok': False,
            'speed': 0.0,
            'stage_completed': False,
            'status': 0,
            'yaw': 0.0,
            'time_since_last_packet': 0,
            'last_packet_time': 0,
            'time': '2022-01-01 00:00:00',
            'stage_name': 'None'
        }
        return vehicleFormat

# GENERAL GET METHOD
#    def get_value(self, key):
#        return next(item for item in self if item[str(key)] == key)
    
# GENERAL SET METHOD
#    def set_value(self, key, value):
#        next(item for item in self if item[str(key)] == key).update({key: value})

#    def get_jsonFormat(self):
#       return self.jsonFormat

    # Setters and Getters  
    
    def setAltitude(self, altitude):
        if(type(altitude) == float):           
            self.update({"altitude": altitude})
    
    def getAltitude(self):
        return self.get("altitude")

    #Add "Altitude color" (Subject to change)
    def setAltitudeColor(self, altitudeColor):
        if(type(altitudeColor) == str):           
            self.update({"altitude_color": altitudeColor})
    
    def getAltitudeColor(self):
        return self.get("altitude_color")
    
    def setBattery(self, battery):
        if(type(battery) == float):           
            self.update({"battery": battery})
    
    def getBattery(self):
        return self.get("battery")

    #Add "Battery color" (Subject to change)
    def setBatteryColor(self, batteryColor):
        if(type(batteryColor) == str):           
            self.update({"battery_color": batteryColor})
    
    def getBatteryColor(self):
        return self.get("battery_color")

    def setCurrentStage(self, stage):
        if(type(stage) == int):           
            self.update({"current_stage": stage})
    
    def getCurrentStage(self):
        return self.get("current_stage")

    def setGeofenceCompliant(self, isCompliant):
        if(type(isCompliant) == bool):           
            self.update({"geoFence_compliant": isCompliant})
    
    def getGeofenceCompliant(self):
        return self.get("geofence_compliant")

    #Add "Geofence Compliant color"
    
    def setLatitude(self, latitude):
        if(type(latitude) == float):           
            self.update({"latitude": latitude})
    
    def getLatitude(self):
        return self.get("latitude")
    
    def setLongitude(self, longitude):
        if(type(longitude) == float):           
            self.update({"longitude": longitude})
    
    def getLongitude(self):
        return self.get("longitude")

    def setPitch(self, pitch):
        if(type(pitch) == float):           
            self.update({"pitch": pitch})
    
    def getPitch(self):
        return self.get("pitch")

    #Add "Pitch color" 

    def setPropulsion(self, propulsion):
        if(type(propulsion) == bool):           
            self.update({"propulsion": propulsion})
    
    def getPropulsion(self):
        return self.get("propulsion")

    #Add "Propulsion color" 

    def setRoll(self, roll):
        if(type(roll) == float):           
            self.update({"roll": roll})
    
    def getRoll(self):
        return self.get("roll")

    #Add "Roll color" 

    def setSensorsOk(self, sensorOk):
        if(type(sensorOk) == bool):           
            self.update({"sensors_ok": sensorOk})
    
    def getSensorsOk(self):
        return self.get("sensors_ok")
    
    def setSpeed(self, speed):
        if(type(speed) == float):           
            self.update({"speed": speed})
    
    def getSpeed(self):
        return self.get("speed")

    def setStageCompleted(self, stageComplete):
        if(type(stageComplete) == bool):           
            self.update({"stage_completed": stageComplete})
    
    def getStageCompleted(self):
        return self.get("stage_completed")

    def setStatus(self, status):
        if(type(status) == int):           
            self.update({"status": status})
    
    def getStatus(self):
        return self.get("status")
        
    def setYaw(self, yaw):
        if(type(yaw) == float):           
            self.update({"yaw": yaw})
    
    def getYaw(self):
        return self.get("yaw")

    def setTimeSinceLastPacket(self, timeSinceLastPacket):
        if(type(timeSinceLastPacket) == int):           
            self.update({"time_since_last_packet": timeSinceLastPacket})
    
    def getTimeSinceLastPacket(self):
        return self.get("time_since_last_packet")
    
    def setLastPacketTime(self, lastPacketTime):
        if(type(lastPacketTime) == int):           
            self.update({"last_packet_time": lastPacketTime})
    
    def getLastPacketTime(self):
        return self.get("last_packet_time")

    def setTime(self, time):
        if(type(time) == str):           
            self.update({"time": time})
    
    def getTime(self):
        return self.get("time")

    def setStageName(self, stageName):
        if(type(stageName) == str):           
            self.update({"stage_name": stageName})
    
    def getStageName(self):
        return self.get("stage_name")