import streamlit as st
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

st.title('Havbøye')
st.subheader('Data frå havbøye')

def start():
    file=open("Havboye-data.csv")
    file.flush()
    
start()
