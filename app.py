# Generate python code for weather analyzing for Creating App.py

import streamlit as st
import pickle

st.title(" Weather Prediction System")

try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    st.error("Model file not found. Please check deployment.")
    st.stop()
# Temperature Analysis
temp_max = st.number_input("Max Temperature", value=20.0)
temp_min = st.number_input("Min Temperature", value=10.0)
precip = st.number_input("Precipitation", value=0.0)
wind = st.number_input("Wind Speed", value=5.0)
# Predict Weather
if st.button("Predict Weather"):
    result = model.predict([[precip, temp_max, temp_min, wind]])
    st.success(f" Weather: {result[0]}")
    def predict_weather(max_temp, min_temp, precipitation, wind_speed):

        features = [[precipitation, max_temp, min_temp, wind_speed]]
        prediction = model.predict(features)
        return prediction[0]