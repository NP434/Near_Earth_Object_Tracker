import streamlit as st
from data import get_data
import numpy as np
import plotly.graph_objects as go


st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()
if objects is None:
    st.write("No data available")

st.title("Near earth Objects")
st.write(f"### Total Near earth objects over past 7 days: {st.session_state['total_count']}")
st.write("Below is a visual representation of the N.E.O.'s distance from the earth "
        "using Lunar units. Lunar units are the distance from the center of the earth to the moon"
        "and is about 385,000 Kilometers, or 239,000 Miles. ")
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0], y=[0],
    mode='markers+text',
    marker=dict(size=20, color='blue'),
    text=["Earth"],
    textposition="top center"
))
scale_factor = 1e-2
for neo in objects:
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

    
fig.update_layout(
    title="Near-Earth Objects Distance Plot (Zoomable)",
    xaxis_title="Distance (scaled)",
    yaxis_title="Distance (scaled)",
    xaxis=dict(scaleanchor="y", scaleratio=1, range =[-0.25,0.25]),
    yaxis=dict(scaleanchor="x", scaleratio=1, range =[-0.25,0.25]),
    showlegend=False,
    hovermode='closest'
)

st.plotly_chart(fig, use_container_width=True)
st.write("DISCLAiMER in the above graph, the angular positon of the markers is not representative of the N.E.O's actual positon, but is used"
        " to demonstrate the distance of the object without clustering the objects in a line.")