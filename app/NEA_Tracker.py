import streamlit as st
from data import get_data
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()

st.title("Near earth Objects over the past week")

neo_list = []
for date_key, neos_on_date in objects.items():
    for neo in neos_on_date:
        neo_entry = {"Date": date_key}
        neo_entry.update(neo)
        neo_list.append(neo_entry)
df = pd.DataFrame(neo_list)
st.dataframe(df, hide_index=True, use_container_width=True)

