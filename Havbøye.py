#Import the required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import csv
import requests

'''
url = 'http://sensor.marin.ntnu.no/logs/Ulstein12345.txt'
#urlretrieve(url, 'Ulstein.csv')
request = Request(url)
response = urlopen(request)
response = response.read()
print (response)
'''

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

'''   
url = 'http://sensor.marin.ntnu.no/logs/Gruppe15.csv'
request = requests.get(url)
print(request.text)
'''
'''
   # Kart 
df = pd.DataFrame(
   np.random.randn(1, 2) / [50, 50] + [62.3433, 5.8488],
   columns=['lat', 'lon'])

st.map(df)
'''

headers = []




df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt", names = ['filename', 'power','loc', 'time', 'lat', 'long','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
st.header("Bar_chart_test")
st.bar_chart(df[['time','lat','long']])
st.dataframe(df)



st.text("Test")

#Kart 2

headers = []




df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein17_10.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
st.header("Bar_chart_test")
st.bar_chart(df[['lat','lon']])
st.dataframe(df)



st.map(df)



st.text("Test")
