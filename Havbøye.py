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

headers = []




df = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'power','loc', 'time', 'lat', 'long','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
st.header("Bar_chart_test")
#st.bar_chart(df[['time','lat','long']])
st.dataframe(df)



st.text("Test")

#Kart 2

headers = []




df = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
st.header("Bar_chart_test")
#st.bar_chart(df[['lat','lon']])
st.dataframe(df)



st.map(df)



st.text("Test")
