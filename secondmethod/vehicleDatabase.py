import sqlite3
from sqlite3 import Error
import json 

if __name__ == '__main__':
    connection = None
    try: 
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        testing = """ CREATE TABLE IF NOT EXISTS testing(altitude FLOAT, altitude_color TEXT, battery TEXT, battery_color TEXT)"""

        vehicle = """ CREATE TABLE IF NOT EXISTS vehicle(altitude FLOAT, altitude_color INTEGER, battery TEXT, battery_color TEXT, current_stage INTEGER,
        geofence_compilant BOOLEAN, geofence_compilant_color TEXT, latitude FLOAT, longitude FLOAT, pitch FLOAT, pitch_color TEXT, propulsion_color TEXT,
        roll FLOAT, roll_color TEXT, sensors_ok BOOLEAN, speed FLOAT, stage_completed BOOLEAN, status INTEGER, yaw FLOAT, time_since_last_packet INTEGER, 
        last_packet_time INTEGER)"""

        cursor.execute(testing)

        json1 = {'altitude': 1.0, 'altitude_color': 'None', 'battery': '85', 'battery_color': 'None' }

        if (json1['altitude'] != 1.0):
            cursor.execute('INSERT INTO testing(altitude, altitude_color) VALUES(:altitude, :altitude_color)', json1)
  
    
        #cursor.execute("SELECT * FROM project WHERE begin_date = '11-05-2021'")
        #results = cursor.fetchall()
        #print(results)

        cursor.execute("SELECT * FROM testing ")
        results = cursor.fetchall()
        print(results)
        connection.commit()

        


    except Error as e: 
        print(e)
    

