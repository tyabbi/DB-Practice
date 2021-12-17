import sqlite3
from sqlite3 import Error
from callVehic import *
import pandas as pd 
import json

# vehicleDatabase.py handles storing vehicle data into a database

#if __name__ == '__main__':

# Values to create connection to SQLite Database
connection = None
dbFile = "database.db"

class vehicleDatabase():

    # Method to save new vehicle dictionary entry to SQLite Database
    def saveData(requestedVehicle):        
        try: 
            # Establish connection with SQLite database "database.db"
            connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
            
            # Enables SQLite commands
            cursor = connection.cursor()

            # TODO: Need to rewrite sql commands with requested vehicle name (hardcoded to testing right now)

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

            # Enters the values into the requested vehicle database
            cursor.execute('INSERT INTO testing(altitude, battery) VALUES(:altitude, :battery)', requestedVehicle)

            # cursor.execute('''INSERT INTO vehicle(altitude, altitude_color, battery, battery_color, current_stage, geofence_compliant,
            #                                    geofence_compliant_color, latitude, longitude, pitch, pitch_color, propulsion, 
            #                                    propulsion_color, roll, roll_color, sensors_ok, speed, stage_completed, status, yaw,
            #                                    time_since_last_packet, last_packet_time) VALUES(:altitude, :altitude_color, :battery, 
            #                                    :battery_color, :current_stage, :geofence_compliant, :geofence_compliant_color, :latitude, 
            #                                    :longitude, :pitch, :pitch_color, :propulsion, :propulsion_color, :roll, :roll_color, :sensors_ok,
            #                                    :speed, :stage_completed, :status, :yaw, :time_since_last_packet, :last_packet_time)''', macVehicle)

            # TEST: Accepting packets under certain conditions
            #if (json1['altitude'] == 1.0):
            #    cursor.execute('INSERT INTO testing(altitude, altitude_color, battery, battery_color) VALUES(:altitude, :altitude_color, :battery, :battery_color)', json1)
            

            # Export the database onto an CSV file
            db_file = pd.read_sql_query("SELECT * FROM testing", connection)
            db_file.to_csv('text_database.csv', index = False)

            connection.commit()
            #connection.close()

        except Error as e: 
            print(e)

    def getData(vehicleName):
        # https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
        try:
            # Establish connection with SQLite database "database.db"
            connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES) 

            # Enables SQLite commands
            cursor = connection.cursor()

            # Select from the requested vehicle database and get the last entry
            execution_line = "SELECT * FROM " + str(vehicleName) + " ORDER BY rowid DESC LIMIT 1"
            cursor.execute(execution_line)
            
            # TODO: try to create dictonary instead of list[dictonary]
            # Create a dictonary for the last entry
            lastEntry = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]

            connection.close()

            return lastEntry

            #one = False
            #return (lastEntry[0] if lastEntry else None) if one else lastEntry
        except Error as e:
            print(e)

