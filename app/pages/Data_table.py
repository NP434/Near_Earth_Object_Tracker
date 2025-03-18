import streamlit as st
from data import get_data
import pandas as pd

objects,total_count = get_data()
units = st.radio("Select the Units: ",("Metric","Imperial"))
st.title("Table view")
df = pd.DataFrame(objects)
if units == "Metric":
    df = df.drop(columns=["Diameter (ft)", "Velocity (miles/h)"], error="ignore")
else:
    df = df.drop(columns=["Diameter (km)", "Velocity (km/h)"], error="ignore")
st.dataframe(df, hide_index=True)