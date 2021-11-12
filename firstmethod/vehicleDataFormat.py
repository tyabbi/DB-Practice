# the format for the packet inputs (standard)
class vehicleDataFormat():
    
    def __init__(self):
        self.jsonFormat = {
            'Altitude': 0.0,
            'Altitude Color': None,
            'Battery': 0.0,
            'Battery Color': None,
            'Current Stage': 0,
            'Geofence Compliant': False,
            'Geofence Compliant Color': None,
            'Latitude': 0.0,
            'Longitude': 0.0,
            'Pitch': 0.0,
            'Pitch Color': None,
            'Propulsion': False,
            'Propulsion Color': None,
            'Roll': 0.0,
            'Roll Color': None,
            'Sensors ok': False,
            'Speed': 0.0,
            'Stage Completed': False,
            'Status': 0,
            'Yaw': 0.0,
            'time_since_last_packet': 0,
            'last_packet_time': 0
        }
    # 'finalized' jsonFormat
    def dataFormat():
        jsonFormat = {
            'Altitude': 0.0,
            'Altitude Color': None,
            'Battery': 0.0,
            'Battery Color': None,
            'Current Stage': 0,
            'Geofence Compliant': False,
            'Geofence Compliant Color': None,
            'Latitude': 0.0,
            'Longitude': 0.0,
            'Pitch': 0.0,
            'Pitch Color': None,
            'Propulsion': False,
            'Propulsion Color': None,
            'Roll': 0.0,
            'Roll Color': None,
            'Sensors ok': False,
            'Speed': 0.0,
            'Stage Completed': False,
            'Status': 0,
            'Yaw': 0.0,
            'time_since_last_packet': 0,
            'last_packet_time': 0
        }
        return jsonFormat

# GENERAL GET METHOD
#    def get_value(self, key):
#        return next(item for item in self if item[str(key)] == key)
    
# GENERAL SET METHOD
#    def set_value(self, key, value):
#        next(item for item in self if item[str(key)] == key).update({key: value})

#    def get_jsonFormat(self):
#       return self.jsonFormat

    def set_altitude(self, altitude):
        if(type(altitude) == float):           
            self.update({"Altitude": altitude})
    
    def get_altitude(self):
        return self.get("Altitude")

    #Add "Altitude color"
    
    def set_battery(self, battery):
        if(type(battery) == float):           
            self.update({"Battery": battery})
    
    def get_battery(self):
        return self.get("Battery")

    #Add "Battery color"

    def set_currentStage(self, stage):
        if(type(stage) == int):           
            self.update({"Current Stage": stage})
    
    def get_currentStage(self):
        return self.get("Current Stage")

    def set_geofenceCompliant(self, is_compliant):
        if(type(is_compliant) == bool):           
            self.update({"GeoFence Compliant": is_compliant})
    
    def get_geofenceCompliant(self):
        return self.get("Geofence Compliant")

    #Add "Geofence Compliant color"
    
    def set_latitude(self, latitude):
        if(type(latitude) == float):           
            self.update({"Latitude": latitude})
    
    def get_latitude(self):
        return self.get("Latitude")
    
    def set_longitude(self, longitude):
        if(type(longitude) == float):           
            self.update({"Longitude": longitude})
    
    def get_longitude(self):
        return self.get("Longitude")

    def set_pitch(self, pitch):
        if(type(pitch) == float):           
            self.update({"Pitch": pitch})
    
    def get_pitch(self):
        return self.get("Pitch")

    #Add "Pitch color" 

    def set_propulsion(self, propulsion):
        if(type(propulsion) == bool):           
            self.update({"Propulsion": propulsion})
    
    def get_propulsion(self):
        return self.get("Propulsion")

    #Add "Propulsion color" 

    def set_roll(self, roll):
        if(type(roll) == float):           
            self.update({"Roll": roll})
    
    def get_roll(self):
        return self.get("Roll")

    #Add "Roll color" 

    def set_sensorsOk(self, sensorOk):
        if(type(sensorOk) == bool):           
            self.update({"Sensors ok": sensorOk})
    
    def get_sensorsOk(self):
        return self.get("Sensors ok")
    
    def set_speed(self, speed):
        if(type(speed) == float):           
            self.update({"Speed": speed})
    
    def get_speed(self):
        return self.get("Speed")

    def set_stageCompleted(self, stageComplete):
        if(type(stageComplete) == bool):           
            self.update({"Stage Completed": stageComplete})
    
    def get_stageCompleted(self):
        return self.get("Stage Completed")

    def set_status(self, status):
        if(type(status) == int):           
            self.update({"Status": status})
    
    def get_status(self):
        return self.get("Status")
        
    def set_yaw(self, yaw):
        if(type(yaw) == float):           
            self.update({"Yaw": yaw})
    
    def get_yaw(self):
        return self.get("Yaw")

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