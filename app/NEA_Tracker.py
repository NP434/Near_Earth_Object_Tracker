import streamlit as st
from data import get_data
import altair as alt
st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()
if objects == None:
    st.write("No data found")

st.title("Near earth Objects over the past week")

st.write(objects)

