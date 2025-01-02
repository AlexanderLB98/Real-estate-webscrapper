import streamlit as st

from src.input_output import load_data
from src.pipeline import apply_pipeline



def data_cleaning_pipeline(selected_files):
    
    st.header("Data cleaning pipeline")
    st.session_state["df"] = load_data(files=selected_files)
    st.write(st.session_state["df"].shape)
    
    
    if st.button("Apply pipeline"):
        df = apply_pipeline(st.session_state["df"])
        st.write(df)
        st.write(df.shape)