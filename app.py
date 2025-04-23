import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Teams and cities list
teams = ['Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Delhi Capitals', 'Chennai Super Kings',
         'Mumbai Indians', 'Rajasthan Royals', 'Punjab Kings', 'Kolkata Knight Riders', 
         'Gujarat Titans', 'Lucknow Super Giants']

cities = ['Bangalore', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai', 'Jaipur', 'Cape Town',
          'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi', 'Bengaluru', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati']

# Page Configuration
st.set_page_config(page_title="IPL Win Predictor 🏏", page_icon="🏆", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #fefcfb;
            background-image: linear-gradient(315deg, #fefcfb 0%, #e7eff9 74%);
            padding: 2rem;
            border-radius: 1rem;
        }
        .title {
            text-align: center;
            color: #FF5733;
            font-size: 3rem;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .result {
            font-size: 1.5rem;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main"><div class="title">🏆 IPL Win Predictor 🏆</div><div class="subtitle">Real-time Match Outcome Predictor for IPL Fans</div>', unsafe_allow_html=True)

# Team Selection
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🏏 Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('🎯 Select the Bowling Team', sorted([team for team in teams if team != batting_team]))

# Venue
selected_city = st.selectbox('📍 Select the Match Venue', sorted(cities))

# Target
target = st.number_input("🎯 Target Score", min_value=1)

# Match Progress
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input("🏏 Current Score", min_value=0)
with col4:
    overs = st.number_input("⏱ Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input("❌ Wickets Fallen", min_value=0, max_value=10)

# Prediction Button
if st.button('📊 Predict Probability'):
    runs_left = target - score
    balls_left = 120 - int(overs * 6)
    wickets = 10 - wickets
    current_run_rate = score / overs 
    required_run_rate = (runs_left * 6) / balls_left 

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[selected_city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets_left':[wickets],
        'total_runs_x':[target],
        'current_run_rate':[current_run_rate],
        'required_run_rate':[required_run_rate]
    })

    # Display input data
    st.markdown("### 📋 Match Situation")
    st.table(input_df)

    # Predict
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    # Display results
    st.markdown(f"<div class='result'><span style='color:#28a745;font-weight:bold;'>{batting_team}</span> chance to win: <strong>{round(win*100)}%</strong></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result'><span style='color:#dc3545;font-weight:bold;'>{bowling_team}</span> chance to win: <strong>{round(loss*100)}%</strong></div></div>", unsafe_allow_html=True)

