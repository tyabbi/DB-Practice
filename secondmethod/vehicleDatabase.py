import sqlite3
from sqlite3 import Error
import json  
import pandas as pd 

if __name__ == '__main__':
    connection = None
    db_file = "database.db"
    try: 
        connection = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
        cursor = connection.cursor()

        testing = """ CREATE TABLE IF NOT EXISTS testing(altitude FLOAT, altitude_color TEXT, battery FLOAT, battery_color TEXT)"""

        vehicle = """ CREATE TABLE IF NOT EXISTS vehicle(altitude FLOAT, altitude_color INTEGER, battery TEXT, battery_color TEXT, current_stage INTEGER,
        geofence_compilant BOOLEAN, geofence_compilant_color TEXT, latitude FLOAT, longitude FLOAT, pitch FLOAT, pitch_color TEXT, propulsion_color TEXT,
        roll FLOAT, roll_color TEXT, sensors_ok BOOLEAN, speed FLOAT, stage_completed BOOLEAN, status INTEGER, yaw FLOAT, time_since_last_packet INTEGER, 
        last_packet_time INTEGER)"""

        cursor.execute(testing)

        json1 = {'altitude': 1.0, 'altitude_color': 'Red', 'battery': 70.0, 'battery_color': 'Blue' }

        if (json1['altitude'] == 1.0):
            cursor.execute('INSERT INTO testing(altitude, altitude_color, battery, battery_color) VALUES(:altitude, :altitude_color, :battery, :battery_color)', json1)

        db_file = pd.read_sql_query("SELECT * FROM testing", connection)
        db_file.to_csv('text_database.csv', index = False)

        #cursor.execute("SELECT * FROM project WHERE begin_date = '11-05-2021'")
        #results = cursor.fetchall()
        #print(results)

        #cursor.execute("SELECT * FROM testing ")
        #results = cursor.fetchall()
        #print(results)

        connection.commit()

        


    except Error as e: 
        print(e)
    

