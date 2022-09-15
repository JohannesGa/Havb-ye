import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye')
st.subheader('Data frå havbøye')

def start():
    #file=open("Havboye-data.csv")
    #file.flush()
    st.file('Havboye-data.csv')
start()
