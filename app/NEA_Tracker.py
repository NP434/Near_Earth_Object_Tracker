import streamlit as st
from data import get_data
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()

st.title("Near earth Objects")
st.write(f"### Total Near earth objects over past 7 days: {st.session_state['total_count']}")
for date_key in st.session_state['daily_counts']:
    st.write(f"Daily counts {date_key}")