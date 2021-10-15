class ToVehicle():
    def data():
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
    def data1():
        json = {
            'Altitude': 0.0,
            'Battery': 0.0,
            'Current Stage': 0,
            'Geofence Compliant': False,
            'Latitude': 0.0,
            'Longitude': 0.0,
            'Pitch': 0.0,
            'Propulsion': False,
            'Roll': 0.0,
            'Sensors ok': False,
            'Speed': 0.0,
            'Stage Completed': False,
            'Status': 0,
            'Yaw': 0.0,
            'time_since_last_packet': 0,
            'last_packet_time': 0
        }
        return json