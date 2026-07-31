import streamlit as st

import pandas as pd

st.title(' 🤖 Machine Learning App')

st.write('This is machine learning app')

df  = pd.read_csv('https://raw.githubusercontent.com/cabled510/RICE-GERMPLASM-CLASSIFICATION-AND-PREDICTION-APP/refs/heads/master/RiceML/Preprocessed_Rice_Data.csv')
df

