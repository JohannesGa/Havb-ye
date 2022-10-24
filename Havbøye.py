#Import the required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import csv
import requests


# Add a title and intro text
st.title('Havbøye')
st.text('Informasjon henta frå havbøye')
# Create file uploader object
upload_file = st.file_uploader('Last opp data om Havbøya')
# Check to see if a file has been uploaded
if upload_file is not None:
   # If it has then do the following:
   # Read the file to a dataframe using pandas
   df = pd.read_csv(upload_file)
   # Create a section for the dataframe statistics
   st.header('Statistics of Dataframe')
   st.write(df.describe())
   # Create a section for the dataframe header
   st.header('Header of Dataframe')
   st.write(df.head())
   

#Kart 2

headers = []




df = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'Power','Strt loc', 'Time', 'Lat', 'Lon','Altitude','Speed','Course','Fix mode','REserved 1','HDOP','PDOP','VDOP','Reserved 2','GPS','GNSS','GLONASS','Reserved 3'])
st.header("Bar_chart_test")
st.bar_chart(df[['lat','lon']])
st.dataframe(df)



st.map(df)
