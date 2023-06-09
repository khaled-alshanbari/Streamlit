import mysql.connector
import streamlit
from mysql.connector import Error
import pandas as pd


def create_db_connection(host_name='sql7.freemysqlhosting.net', user_name='sql7609688', user_password='zueRf6BIf4', db_name='sql7609688'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        streamlit.info("MySQL Database connection successful")
        
    except Error as err:
        streamlit.info(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = None
    try:
        cursor = connection.cursor()
    except Exception:
        cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        streamlit.info("Query successful")
    except Error as err:
        streamlit.info(f"Error: '{err}'")

def read_query(connection, query):
    cursor = None
    try:
        cursor = connection.cursor()
        result = None
    except Exception:
        streamlit.info("Starting MySQL Server....")
        cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        streamlit.info("Info Pull successful")
        return result
    except Error as err:
        streamlit.info(f"Error: '{err}'")
