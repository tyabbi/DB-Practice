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
            'last_packet_time': 0
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
            'last_packet_time': 0
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
    
    def set_altitude(self, altitude):
        if(type(altitude) == float):           
            self.update({"altitude": altitude})
    
    def get_altitude(self):
        return self.get("altitude")

    #Add "Altitude color"
    
    def set_battery(self, battery):
        if(type(battery) == float):           
            self.update({"battery": battery})
    
    def get_battery(self):
        return self.get("battery")

    #Add "Battery color"

    def set_currentStage(self, stage):
        if(type(stage) == int):           
            self.update({"current_Stage": stage})
    
    def get_currentStage(self):
        return self.get("current_stage")

    def set_geofenceCompliant(self, is_compliant):
        if(type(is_compliant) == bool):           
            self.update({"geoFence_compliant": is_compliant})
    
    def get_geofenceCompliant(self):
        return self.get("geofence_compliant")

    #Add "Geofence Compliant color"
    
    def set_latitude(self, latitude):
        if(type(latitude) == float):           
            self.update({"latitude": latitude})
    
    def get_latitude(self):
        return self.get("latitude")
    
    def set_longitude(self, longitude):
        if(type(longitude) == float):           
            self.update({"longitude": longitude})
    
    def get_longitude(self):
        return self.get("longitude")

    def set_pitch(self, pitch):
        if(type(pitch) == float):           
            self.update({"pitch": pitch})
    
    def get_pitch(self):
        return self.get("pitch")

    #Add "Pitch color" 

    def set_propulsion(self, propulsion):
        if(type(propulsion) == bool):           
            self.update({"propulsion": propulsion})
    
    def get_propulsion(self):
        return self.get("propulsion")

    #Add "Propulsion color" 

    def set_roll(self, roll):
        if(type(roll) == float):           
            self.update({"roll": roll})
    
    def get_roll(self):
        return self.get("roll")

    #Add "Roll color" 

    def set_sensorsOk(self, sensorOk):
        if(type(sensorOk) == bool):           
            self.update({"sensors_ok": sensorOk})
    
    def get_sensorsOk(self):
        return self.get("sensors_ok")
    
    def set_speed(self, speed):
        if(type(speed) == float):           
            self.update({"speed": speed})
    
    def get_speed(self):
        return self.get("speed")

    def set_stageCompleted(self, stageComplete):
        if(type(stageComplete) == bool):           
            self.update({"stage_completed": stageComplete})
    
    def get_stageCompleted(self):
        return self.get("stage_completed")

    def set_status(self, status):
        if(type(status) == int):           
            self.update({"status": status})
    
    def get_status(self):
        return self.get("status")
        
    def set_yaw(self, yaw):
        if(type(yaw) == float):           
            self.update({"yaw": yaw})
    
    def get_yaw(self):
        return self.get("yaw")

    def set_time_since_last_packet(self, time_since_last_packet):
        if(type(time_since_last_packet) == int):           
            self.update({"time_since_last_packet": time_since_last_packet})
    
    def get_time_since_last_packet(self):
        return self.get("time_since_last_packet")

    
    def set_last_packet_time(self, last_packet_time):
        if(type(last_packet_time) == int):           
            self.update({"last_packet_time": last_packet_time})
    
    def get_last_packet_time(self):
        return self.get("last_packet_time")