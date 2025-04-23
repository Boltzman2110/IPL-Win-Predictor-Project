import streamlit as st
import pickle
import pandas as pd

with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

teams = ['Sunrisers Hyderabad',
         'Royal Challengers Bangalore',
         'Delhi Capitals',
         'Chennai Super Kings',
         'Mumbai Indians',
         'Rajasthan Royals',
         'Punjab Kings',
         'Kolkata Knight Riders',
         'Gujarat Titans',
         'Lucknow Super Giants']

cities = ['Bangalore', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai',
          'Jaipur', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
          'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
          'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune',
          'Raipur', 'Ranchi', 'Abu Dhabi', 'Bengaluru', 'Dubai',
          'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati']

pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted(teams))

selected_city = st.selectbox('Select the host city', sorted(cities))

target = st.number_input("Target Score", min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input("Current Score")
with col4:
    overs = st.number_input("Overs completed")
with col5:
    wickets = st.number_input("Wickets out")

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    current_run_rate = score / overs
    required_run_rate = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets],
        'total_runs_x': [target],
        'current_run_rate': [current_run_rate],
        'required_run_rate': [required_run_rate]
    })
    st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "-" + str(round(win * 100)) + "%")
    st.header(bowling_team + "-" + str(round(loss * 100)) + "%")
