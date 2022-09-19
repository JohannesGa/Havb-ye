#Import the required Libraries
import streamlit as st
import pandas as pd

# Add a title and intro text
st.title('Havbøye')
st.text('Informasjon henta frå havbøye')
# Create file uploader object
upload_file = st.file_uploader('Upload a file containing earthquake data')
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
   
