"""
Author: Noah Perea
Date: 3/18/2025
Purpose: Homepage of the NEO tracker site
Credit: Chat gpt was used to fix errors regarding display, and for the syntax of creating the plotly diagram.
"""
import streamlit as st
import numpy as np
import plotly.graph_objects as go
st.set_page_config( # Placed to allow the test to function without the need for the API_KEY.
    page_title="Near Earth Asteroid Tracker"
)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #87CEEB, #000000);
        color: white;
    }
    .stApp {
        color: white;
    }

    .stRadio > div {
        background-color: transparent;
    }
    </style>
    
    .stSelectbox, .stTextInput, .stButton, .stDataFrame {
        background-color: transparent;
        color: white;
    }
    """,
    unsafe_allow_html=True
)
from data import get_data,reset_cache

objects, total_count = get_data()



st.title("Near earth Objects")
if objects is None:
    st.write("### API Fetch Failed, No data Currently avaialble")
else:
    st.write(f"### Total Near earth objects over past 7 days: {total_count}")
    refresh_button = st.sidebar.button("Refresh", type="primary", on_click=reset_cache) 
    st.write("Below is a visual representation of the N.E.O.'s distance from the earth "
        "using Lunar units. Lunar units are the distance from the center of the earth to the moon"
        " and is about 385,000 Kilometers, or 239,000 Miles. ")
    #The below code is used to create the figure on the homepage of the site, this figure has a representation of earth, with 
    #    scaled distance of each neo, depicted at different angular positions to preven clustering
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers+text',
        marker=dict(size=20, color='blue'),
        text=["Earth"],
        textposition="top center"
    ))
    scale_factor = 1e-2 #used to scale the data to improve visibility
    for neo in objects:  #Iterates over each neo and adds them to the figure
        distance = neo["Miss Distance (Lunar)"] * scale_factor
        angle = np.random.uniform(0,2* np.pi)
        x = (distance + 0.01) * np.cos(angle)
        y = (distance + 0.01)  * np.sin(angle)
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=6, color='red'),
            text=[f"{neo['Name']}"],
            textposition="bottom right",
            textfont=dict(size=8)
        ))

    
    fig.update_layout(  #Sets the description and starting zoom level of the figure
        title="Near-Earth Objects Distance from Earth",
        xaxis_title="Distance (scaled), Lunar units",
        yaxis_title="Distance (scaled), Lunar Units",
        xaxis=dict(scaleanchor="y", scaleratio=1, range =[-0.25,0.25]),
        yaxis=dict(scaleanchor="x", scaleratio=1, range =[-0.25,0.25]),
        showlegend=False,
        hovermode='closest'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write("DISCLAIMER: in the above graph, the angular position of the markers is not representative of the N.E.O's actual position, but is used"
            " to demonstrate the distance of the object without clustering the objects in a line. This also results in the angular position of each object varying when refreshing the data,"
            "but the distance remains the same.")