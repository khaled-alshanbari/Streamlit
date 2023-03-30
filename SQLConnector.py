import os
import time

import mysql.connector
import streamlit
from mysql.connector import Error
import pandas as pd


def create_db_connection(host_name='localhost', user_name='root2', user_password='root', db_name='AirForceStatisticalEngine'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = None
    try:
        cursor = connection.cursor()
    except Exception:
        os.system('service mysql start')
        time.sleep(2)
        cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = None
    try:
        cursor = connection.cursor()
        result = None
    except Exception:
        streamlit.info("Starting MySQL Server....")
        os.system('service mysql start')
        time.sleep(5)
        cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def __Create_Tabels(connection):
    create_teacher_table = """
    CREATE TABLE PAPs (
      MAC VARCHAR(255) PRIMARY KEY,
      SSID VARCHAR(255) NOT NULL,
      CH VARCHAR(255) NOT NULL,
      RSSI VARCHAR(255) NOT NULL,
      BeaconInterval VARCHAR(255) NOT NULL,
      Encryption VARCHAR(255) NOT NULL
      );
     """
    execute_query(connection,create_teacher_table)

def __Create_PAPstat_Tables(connection):
    create_teacher_table = """
        CREATE TABLE PAPstat (
          ID int NOT NULL AUTO_INCREMENT,
          Domain VARCHAR(255),
          SSID VARCHAR(255) NOT NULL,
          MAC VARCHAR(255) NOT NULL,
          HOP VARCHAR(255) NOT NULL,
          RTT VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID)
          );
         """
    execute_query(connection, create_teacher_table)
def __Create_PAPstat_Extra_Tables(connection):
    create_teacher_table = """
        CREATE TABLE PAPExtraStat (
          ID int NOT NULL AUTO_INCREMENT,
          PublicIP VARCHAR(255) NOT NULL,
          Stations VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID)
          );
         """
    execute_query(connection, create_teacher_table)
