import sqlite3
from sqlite3 import Error
from updateVehicle import *
import pandas as pd 

# used to create data for frontend

# Values to create connection to SQLite Database
connection = None
dbFile = "database.db"
try: 
    # Establish connection with SQLite database "database.db"
    connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)

    # Enables SQLite commands
    cursor = connection.cursor()

    # TEST: Tests creating a table
    # testingTable = """ CREATE TABLE IF NOT EXISTS MEA(latitude FLOAT, longitude FLOAT, battery INT, mode STRING, last_packet_time INTEGER, current_stage INTEGER) """
    # # # Creates the table
    # cursor.execute(testingTable)



    databaseLine = "SELECT * FROM ERU"
    csvTitle = "ERU_database.csv"
    db_file = pd.read_sql_query(databaseLine, connection)
    db_file.to_csv(csvTitle, index = False)
    
    # how to delete tables 
    # cursor.execute("DROP table MEA")
    
    connection.close()

except Error as e: 
    print(e)