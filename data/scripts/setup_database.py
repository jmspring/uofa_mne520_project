#!/usr/bin/env python3

# Jim Spring
# MNE 520
# This script is used to create the database and tables necessary to import the
# consolidated MRDS database.  Additionally, it imports the data into the MSSQL
# instance.
#  
# This script relies on the pymssql - https://pypi.org/project/pymssql/ being 
# installed.
#
# Usage: setup_database.py <host> <port> <user> <password>
import pymssql
import sys
import os

# Globals
DATABASE_NAME = "mrds"
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

# create database connection
def create_db_connection(host, port, username, password):
    conn = None
    try:
        conn = pymssql.connect(server=host, port=port, user=username, password=password)
    except pymssql.InterfaceError:
        print("A MSSQLDriverException has been caught.")
    except pymssql.DatabaseError:
        print("A MSSQLDatabaseException has been caught.")
    return conn

# create the database
#   this function will drop the database first if it exists
def create_database(conn):
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS {0};".format(DATABASE_NAME))
    cursor.execute("CREATE DATABASE {0};".format(DATABASE_NAME))
    conn.autocommit(False)

# execute sql commands in file
#   this function is a helper function fhat takes a handle to the database
#   connection and a path to the SQL file to execute
def execute_sql_file(conn, sqlFile):
    # read the sql file to a string
    sqlFileHandle = open(sqlFile, 'r')
    sql = sqlFileHandle.read()
    sqlFileHandle.close()

    # execute the sql
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.autocommit(False)

# create table suitable for mrds data
#   this script assumes the file `mrds-csv.sql` lives in the directory `sql`
#   which is at the same level as this script
def create_mrds_schema(conn):
    # generate path to the schema file
    schemaFile = os.path.abspath("{0}/../sql/mrds-csv.sql".format(SCRIPT_PATH))

    # execute the SQL
    execute_sql_file(conn, schemaFile)

# import the mrds data
#   this function assumes that the MRDS csv file that was downloaded has been placed
#   on the system where SQL Server is running.  data is imported using the BULK INSERT
#   command which requires the data be in the same system.  since this example is using
#   Docker, the CSV file is mapped into `/tmp/mrds.csv`
def import_mrds_data(conn):
    # generate path to the bulk load sql file
    dataImportFile = os.path.abspath("{0}/../sql/mrds-data-load.sql".format(SCRIPT_PATH))

    # execute the SQL
    execute_sql_file(conn, dataImportFile)

def generate_mrds_geospation_point(conn):
    # generate path to the geospatial sql update
    geoUpdateFile = os.path.abspath("{0}/../sql/mrds-csv-add-geo.sql".format(SCRIPT_PATH))

    # execute the SQL
    execute_sql_file(conn, geoUpdateFile)    

if __name__=="__main__":
    if len(sys.argv) != 5:
        print("Usage: {0} <host> <port> <user> <password>".format(sys.argv[0]))
        sys.exit(1)
    dbHost = sys.argv[1]
    dbPort = int(sys.argv[2])
    dbUsername = sys.argv[3]
    dbPassword = sys.argv[4]

    # retrieve the database connection
    print("connecting to database...")
    conn = create_db_connection(dbHost, dbPort, dbUsername, dbPassword)
    if conn == None:
        print("Unable to connect to database.")
        sys.exit(1)

    # create the database
    print("creating database...")
    create_database(conn)

    # create the tables for mrds
    print("create mrds schema...")
    create_mrds_schema(conn)

    # import the mrds data
    print("import mrds data into database...")
    import_mrds_data(conn)