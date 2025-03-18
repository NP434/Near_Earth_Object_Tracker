import streamlit as st
from data import get_data
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()

st.title("Near earth Objects")
total_objects = 0
counts = {}
for date, date_data in objects.items():
    if date != "total_objects":
        daily_count = len(date_data)
        counts[date] = daily_count
        total_objects += daily_count



st.write(f"### Total number of objects over past 7 days: {total_objects}")
st.write("### NEO Count Per Day:")
for date, count in counts.items():
    st.write(f"**{date}**: {count} NEO(s)")
chart_data = pd.DataFrame(counts, columns= counts[date])
st.bar_chart(chart_data)

