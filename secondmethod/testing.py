import sqlite3
from sqlite3 import Error
from updateVehicle import *
import pandas as pd 
from datetime import datetime

# used for testing 

now = datetime.now()
# print(now)

# oldTime = now.replace(hour=12, minute=0, second=0, microsecond=0).time()
# # the latest stage
# generalStage = 0

# # New Time
# newestPacketTime = now.replace(hour=14, minute=5, second=0, microsecond=0).time()

# newData = {"vehicle_name": "testing",
#             "altitude": 100.0,
#             "altitude_color": "Red",
#             "battery": 25.0,
#             "time": str(newestPacketTime)}


# x = newData['time']
# jsonTime = datetime.strptime(x, '%H:%M:%S')
# newTime = jsonTime.time()
# newStage = 1

# print("old info")
# print(oldTime)
# print(generalStage)

# # compare the old time/stage with the new time/stage
# if (newTime > oldTime):
#     oldTime = newTime
#     generalStage = newStage

# print("new info")
# print(oldTime)
# print(generalStage)

#Values to create connection to SQLite Database
connection = None
dbFile = "database.db"


connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
            
# Enables SQLite commands
cursor = connection.cursor()

x = {
    'altitude': 87.25, 
    'current_stage': 0,
    'time': str(now)
}

# TEST: Tests creating a table
testingTable = """ CREATE TABLE IF NOT EXISTS testing(altitude FLOAT, current_stage INTEGER, time STRING)"""
cursor.execute(testingTable)

execution = '''INSERT INTO testing(altitude, current_stage, time) VALUES(:altitude, :current_stage, :time)'''
cursor.execute(execution, x)



# used to create data for frontend

# Values to create connection to SQLite Database
# connection = None
# dbFile = "database.db"
# try: 
#     # Establish connection with SQLite database "database.db"
#     connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)

#     # Enables SQLite commands
#     cursor = connection.cursor()

#     # TEST: Tests creating a table
#     # testingTable = """ CREATE TABLE IF NOT EXISTS MEA(latitude FLOAT, longitude FLOAT, battery INT, mode STRING, last_packet_time INTEGER, current_stage INTEGER) """
#     # # # Creates the table
#     # cursor.execute(testingTable)



#     databaseLine = "SELECT * FROM ERU"
#     csvTitle = "ERU_database.csv"
#     db_file = pd.read_sql_query(databaseLine, connection)
#     db_file.to_csv(csvTitle, index = False)
    
#     # how to delete tables 
#     # cursor.execute("DROP table MEA")
    
#     connection.close()

# except Error as e: 
#     print(e)