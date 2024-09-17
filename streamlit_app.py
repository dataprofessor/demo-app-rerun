import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Hello world!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/population-dashboard/master/data/us-population-2010-2019-reshaped.csv")
df
