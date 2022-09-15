import streamlit as st
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

st.title('Havbøye')
st.subheader('Data frå havbøye')

csvfile = 'data.csv'
delimiter = ','

def open_with_python_csv(Havboye-data.csv):
  data = []
    with open(Havboye-data.csv, 'r') as filename:
        reader = csv.reader(Havboye-data.csv, delimiter=delimiter)


''' 
def start():
    file=open("Havboye-data.csv","a")
    file.flush()
    file.close()
   ''' 
start()
