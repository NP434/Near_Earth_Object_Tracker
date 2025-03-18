import streamlit as st
from data import get_data,reset_cache
import pandas as pd

objects,total_count = get_data()

st.title("Table view")
refresh_button = st.sidebar.button("Refresh", type="primary", on_click=reset_cache)
col1, col2 =st.columns(2, border = True)
with col2:
    units = st.radio("Select the Units: ",("Metric","Imperial"),horizontal=True)
df = pd.DataFrame(objects)
if units == "Metric":
    df = df.drop(columns=["Diameter (ft)", "Velocity (miles/h)"], errors="ignore")
else:
    df = df.drop(columns=["Diameter (km)", "Velocity (km/h)"], errors="ignore")
with col1:
    st.dataframe(df, hide_index=True)