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
            #exctract the NEO's for the given date and the specified characteristics of each NEO
            neo_dict = {date_key: [{ "name": neo['name'],
                                "diameter km":int(neo['estimated_diameter']['kilometers']['estimated_diameter_max']),
                                "diameter ft":neo['estimated_diameter']['feet']['estimated_diameter_max'],
                                'hazardous': neo['is_potentially_hazardous_asteroid'],
                                "velocity_Km": neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'],
                                "velocity_miles": neo['close_approach_data'][0]['relative_velocity']['miles_per_hour'],
                                "miss_distance_km": neo['close_approach_data'][0]['miss_distance']['kilometers'],
                                "miss_distance_miles": neo['close_approach_data'][0]['miss_distance']['miles']
                                } for neo in neos_on_date ] for date_key, neos_on_date in neos_data.items() }
            return neo_dict
    except Exception as e:
        print(e)
