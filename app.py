import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

import os
import pickle

# Replace 'file_path' with the path to your 'pipe.pkl' file
file_path = 'C:/Users/SIDDHARTH/Downloads/ODI_pipe.pkl'  # Substitute this with your actual file path

if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        pipe = pickle.load(file)
else:
    print(f"File '{file_path}' not found.")

#pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka',
 'Ireland',
 'Zimbabwe']


st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

col3,col4,col5,col6,col7,col8,col9 = st.columns(7)

with col3:
     total_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done')
with col5:
    total_wickets = st.number_input('Wickets out')
with col6:
    prev_60balls_run= st.number_input('Runs scored in last 10 overs')
with col7:
    prev_60balls_wickets= st.number_input('wickets out in last 10 overs')
with col8:
    prev_60balls_dots= st.number_input('dots in last 10 overs')
with col9:
    prev_60balls_boundaries= st.number_input('boundaries in last 10 overs')

if st.button('Predict Score'):
   

    input_df = pd.DataFrame(
    { 'batting_team':[batting_team],'bowling_team':[ bowling_team],	'overs':[ overs], 'total_score':[total_score],	'total_wickets':[total_wickets],	'prev_60balls_run':[prev_60balls_run],	'prev_60balls_wickets':[prev_60balls_wickets],	'prev_60balls_dots':[prev_60balls_dots],	'prev_60balls_boundaries':[prev_60balls_boundaries]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
