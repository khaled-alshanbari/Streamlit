import streamlit as st

from SQLConnector import *
st.set_page_config(page_title="AirForce Security", layout='wide')

connection = create_db_connection()

out = read_query(connection, "select * from streamlit"):

st.write(out)
