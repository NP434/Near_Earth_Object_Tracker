import streamlit as st
from data import get_data
import pandas as pd

objects,total_count = get_data()

st.title("Table view")
col1, col2 =st.columns([3,1])
units = col2.st.radio("Select the Units: ",("Metric","Imperial"))
df = pd.DataFrame(objects)
if units == "Metric":
    df = df.drop(columns=["Diameter (ft)", "Velocity (miles/h)"], errors="ignore")
else:
    df = df.drop(columns=["Diameter (km)", "Velocity (km/h)"], errors="ignore")
col1.st.dataframe(df, hide_index=True)