import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye')


 
def start():
    response=send_at_get_resp("AT+CGNSINF")
    print("Ulstein TOF2 Bøye nr1 "+response)
    file=open("data.csv","a")
    file.write(str(response)+",")
    file.flush()
    file.close()
    
start()
