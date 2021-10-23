# the format for the packet inputs (standard)
class vehicleDataFormat():
    
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

    # alternative format
    def data1():
        jsonFormat = [{
            {
                'title': 'Altitude',
                'value': 0.0
            },
            {
                'title':'Battery',
                'value': 0.0            
            },
            { 
                'title':'Current Stage',
                'value': 0
            }, 
            {
                'title':'GeoFence Compliant',
                'value': False
            },
            {
                'title':'Latitude',
                'value': 0.0
            },
            {
                'title':'Longitude',
                'value': 0.0
            }, 
            {
                'title':'Pitch',
                'value': 0.0
            },
            {
                'title':'Propulsion',
                'value': False
            }, 
            {
                'title':'Roll',
                'value': 0.0
            }, 
            {
                'title':'Sensors OK',
                'value': False
            }, 
            {
                'title':'Speed',
                'value': 0.0
            },
            {
                'title':'Stage Completed',
                'value': False
            },
            {
                'title':'Status',
                'value': 0
            },
            {
                'title':'Yaw',
                'value': 0.0
            },
            {
                'title':'Time_since_last packet',
                'value': 0
            },
            {
                'title': 0,
                'value': 0
            } 
            
        }]
        return jsonFormat
    