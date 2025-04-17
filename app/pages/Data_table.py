"""
Author: Noah Perea
Date: 3/18/2025
Purpose:This is the page that displays the data table view of the processed data
"""
import streamlit as st
from data import get_data,reset_cache
import pandas as pd
st.markdown(
    """
    <style>
    html, body [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #000000 40%, #00BFFF);
        color: white;
    }
    .stApp {
        color: white;
    }

    .stRadio > div {
        background-color: transparent;
        
    }
    .stSelectbox, .stTextInput, .stButton, .stDataFrame {
        background-color: transparent;
        color: white;
    }
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
    }
    thead tr th {
        color: white !important;
    }
        .css-ffhzg2 {  /* sometimes used for headers and labels */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

objects,total_count = get_data() # get data and total count

st.title("Table view") 

if objects is None: #If API fetch failed
    st.write("### API Fetch Failed, No data Currently avaialble")
else:
    refresh_button = st.sidebar.button("Refresh", type="primary", on_click=reset_cache)
    units = st.radio("Select the Units: ",("Metric","Imperial"), horizontal=True) #Sets the units for use in the table
    df = pd.DataFrame(objects)
    if units == "Metric": # Removes imperial unit columns
        df = df.drop(columns=["Diameter (ft)", "Velocity (miles/h)"], errors="ignore")
    else: #Removes Metric unit columns
        df = df.drop(columns=["Diameter (km)", "Velocity (km/h)"], errors="ignore")
    st.dataframe(df, hide_index=True, use_container_width=True) #Places the table in column one