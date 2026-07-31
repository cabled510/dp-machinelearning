import streamlit as st

import pandas as pd

st.title('🌾 LEVERAGING MACHINE LEARNING FOR PRECISION CLASSIFICATION AND PHENOTYPIC PREDICTION OF GHANAIAN RICE GERMPLASM')

st.write('This is machine learning app')


with st.expander('Data'):
  st.write('**Preprocessed Rice Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/cabled510/RICE-GERMPLASM-CLASSIFICATION-AND-PREDICTION-APP/refs/heads/master/RiceML/Full%20Dataset.csv')
  df



st.write('**X**')
  X = df.drop('Accession', axis=1)
  X






