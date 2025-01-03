import streamlit as st

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
