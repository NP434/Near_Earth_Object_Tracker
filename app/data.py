from json import dump, load
from datetime import date
from dateutil import tz
from requests import get
import streamlit as st
import os

API_KEY = st.secrets["API_KEY"]

def get_data() -> dict:

    current_date = date.today()
    start_date = (current_date.replace(day = current_date.day - 7)) 
    try:
        response = get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={current_date}&api_key={API_KEY}")
        raw_data = response.json()
        if raw_data is None:
            neo_dict = None
        else:
            with open("asteroids.json", "w") as file:
                dump(raw_data, file, indent = 4, sort_keys= True)
            neos_data = raw_data.get('near_earth_objects', {})
           
            neo_lst = []
            total_neos = 0
            for date_key, neos_per_date in neos_data.items():
                total_neos = len(neos_per_date)
                
                neo_lst.extend = [{
                    "Date": date_key,
                    "Name": neo['name'],
                    "Diameter (km)": round(neo['estimated_diameter']['kilometers']['estimated_diameter_max'], 2),
                    "Diameter (ft)": round(neo['estimated_diameter']['feet']['estimated_diameter_max'], 2),
                    "Hazardous": neo['is_potentially_hazardous_asteroid'],
                    "Velocity (km/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']), 2),
                    "Velocity (miles/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['miles_per_hour']), 2),
                    "Miss Distance (km)": round(float(neo['close_approach_data'][0]['miss_distance']['kilometers']), 2),
                    "Miss Distance (miles)": round(float(neo['close_approach_data'][0]['miss_distance']['miles']), 2)
                } for neo in neos_per_date ]
                st.session_state["total_count"] = total_neos
            return neo_lst
    except Exception as e:
        print(e)

