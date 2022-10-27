import csv
import streamlit as st
import pandas as pd
import numpy as np
import requests
from link_button import link_button


headers = []

st.title('Havbøye prosjekt')

df1 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB1.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Temperature'])
df2 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB2.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Temperature'])
df3 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB3.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Temperature'])
df4 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB4.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Temperature'])
df5 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB5.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Temperature'])

st.header('Informasjon om bøye 1')
st.dataframe(df1)
st.map(df1)

link_button('Data fra maritim', 'http://sensor.marin.ntnu.no/logs/UlsteinB1.txt')



st.header('Informasjon om bøye 2')
st.dataframe(df2)
st.map(df2)

url2 = 'http://sensor.marin.ntnu.no/logs/UlsteinB2.txt'

if st.button('Data fra maritim'):
    webbrowser.open_new_tab(url2)

st.header('Informasjon om bøye 3')
st.dataframe(df3)
st.map(df3)

url3 = 'http://sensor.marin.ntnu.no/logs/UlsteinB3.txt'

if st.button('Data fra maritim'):
    webbrowser.open_new_tab(url3)

st.header('Informasjon om bøye 4')
st.dataframe(df4)
st.map(df4)

url4 = 'http://sensor.marin.ntnu.no/logs/UlsteinB4.txt'

if st.button('Data fra maritim'):
    webbrowser.open_new_tab(url4)

st.header('Informasjon om bøye 5')
st.dataframe(df5)
st.map(df5)

url5 = 'http://sensor.marin.ntnu.no/logs/UlsteinB5.txt'

if st.button('Data fra maritim'):
    webbrowser.open_new_tab(url5)
