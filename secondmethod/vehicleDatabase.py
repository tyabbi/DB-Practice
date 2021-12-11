import sqlite3
from sqlite3 import Error
from callVehic import *
import pandas as pd 

# vehicleDatabase.py handles storing vehicle data into a database

#if __name__ == '__main__':

class vehicleDatabase():

    def saveData(macVehicle):
        connection = None
        db_file = "database.db"

        try: 
            # Establish connection with SQLite database "database.db"
            connection = sqlite3.connect(db_file, isolation_level=None,
                            detect_types=sqlite3.PARSE_COLNAMES)
            
            # Enables SQLite commands
            cursor = connection.cursor()

            # TEST: Tests creating a table
            testing = """ CREATE TABLE IF NOT EXISTS testing(altitude FLOAT, altitude_color TEXT, battery FLOAT, battery_color TEXT)"""

            # Create an empty table with the vehicle data. 
            # Parameters follow the format (varName, TYPE). 
            vehicle = """ CREATE TABLE IF NOT EXISTS vehicle(altitude FLOAT, 
                                                                altitude_color TEXT, 
                                                                battery FLOAT, 
                                                                battery_color TEXT, 
                                                                current_stage INTEGER,
                                                                geofence_compliant BOOLEAN, 
                                                                geofence_compliant_color TEXT, 
                                                                latitude FLOAT, 
                                                                longitude FLOAT, 
                                                                pitch FLOAT, 
                                                                pitch_color TEXT, 
                                                                propulsion BOOLEAN,
                                                                propulsion_color TEXT,
                                                                roll FLOAT, 
                                                                roll_color TEXT, 
                                                                sensors_ok BOOLEAN, 
                                                                speed FLOAT, 
                                                                stage_completed BOOLEAN, 
                                                                status INTEGER, 
                                                                yaw FLOAT, 
                                                                time_since_last_packet INTEGER, 
                                                                last_packet_time INTEGER)"""

            # Creates the table
            cursor.execute(testing)

            #macVehicle = callVehicles.macVehicle()
            #print(macVehicle)
            # TEST: Tests adding values to a JSON array
            json1 = {'altitude': 1.0, 'altitude_color': 'Red', 'battery': 70.0, 'battery_color': 'Blue' }

            # cursor.execute('''INSERT INTO vehicle(altitude, altitude_color, battery, battery_color, current_stage, geofence_compliant,
            #                                    geofence_compliant_color, latitude, longitude, pitch, pitch_color, propulsion, 
            #                                    propulsion_color, roll, roll_color, sensors_ok, speed, stage_completed, status, yaw,
            #                                    time_since_last_packet, last_packet_time) VALUES(:altitude, :altitude_color, :battery, 
            #                                    :battery_color, :current_stage, :geofence_compliant, :geofence_compliant_color, :latitude, 
            #                                    :longitude, :pitch, :pitch_color, :propulsion, :propulsion_color, :roll, :roll_color, :sensors_ok,
            #                                    :speed, :stage_completed, :status, :yaw, :time_since_last_packet, :last_packet_time)''', macVehicle)

            # TEST: Tests accepting packets under certain conditions
            #if (json1['altitude'] == 1.0):
            #    cursor.execute('INSERT INTO testing(altitude, altitude_color, battery, battery_color) VALUES(:altitude, :altitude_color, :battery, :battery_color)', json1)
            cursor.execute('INSERT INTO testing(altitude, battery) VALUES(:altitude, :battery)', macVehicle)

            # Export the database onto an CSV file
            #db_file = pd.read_sql_query("SELECT * FROM testing", connection)
            #db_file.to_csv('vehicle_database.csv', index = False)

            #cursor.execute("SELECT * FROM project WHERE begin_date = '11-05-2021'")
            #results = cursor.fetchall()
            #print(results)

            #cursor.execute("SELECT * FROM testing ")
            #results = cursor.fetchall()
            #print(results)

            connection.commit()

        except Error as e: 
            print(e)