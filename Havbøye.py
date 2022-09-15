import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye')
st.subheader('Data frå havbøye')
 
def start():
    file=open("Havbøye-data.csv","a")
    file.flush()
    file.close()
    
start()
