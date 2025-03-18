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
            neo_list = None
        else:
            with open("asteroids.json", "w") as file:
                dump(raw_data, file, indent = 4, sort_keys= True)
            neos_data = raw_data.get('near_earth_objects', {})
           
        neo_list = []  # Flat list for display
        total_count = 0  # Track total count
        daily_counts = []
        for date_key, neos_on_date in neos_data.items():
            day_count = len(neos_on_date)  # Update total count
            total_count += day_count
            daily_counts[date_key] = day_count

            # Process NEO details and append to neo_list
            neo_list.extend([
                {
                    "Date": date_key,
                    "Name": neo['name'],
                    "Diameter (km)": round(neo['estimated_diameter']['kilometers']['estimated_diameter_max'], 2),
                    "Diameter (ft)": round(neo['estimated_diameter']['feet']['estimated_diameter_max'], 2),
                    "Hazardous": neo['is_potentially_hazardous_asteroid'],
                    "Velocity (km/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']), 2),
                    "Velocity (miles/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['miles_per_hour']), 2),
                    "Miss Distance (km)": round(float(neo['close_approach_data'][0]['miss_distance']['kilometers']), 2),
                    "Miss Distance (miles)": round(float(neo['close_approach_data'][0]['miss_distance']['miles']), 2)
                } for neo in neos_on_date
            ])

        st.session_state["total_count"] = total_count  # Store total count in Streamlit state
        st.session_state["daily_counts"] = daily_counts  # Store total count in Streamlit state
        return neo_list
    except Exception as e:
        print(e)

