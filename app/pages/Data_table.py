import streamlit as st
from data import get_data
import pandas as pd

objects = get_data()

st.title("Table view")
df = pd.DataFrame(objects)
st.dataframe(df, hide_index=True)