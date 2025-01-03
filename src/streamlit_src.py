import os
import streamlit as st

from src.input_output import load_data
from src.pipeline import apply_pipeline
from src.utils import convert_df


def data_cleaning_pipeline(selected_files):
    st.header("Data cleaning pipeline")
    st.session_state["df"] = load_data(files=selected_files)
    st.write(st.session_state["df"].shape)
    
    if st.button("Apply pipeline"):
        st.session_state["df"] = apply_pipeline(st.session_state["df"])
        st.write(st.session_state["df"])
        st.write(st.session_state["df"].shape)
        cities = st.session_state["df"]["city"].unique()
        filename = [str(city) for city in cities]
        filename = "_".join(filename)
        filename = "processed_data-" + filename + ".csv"
        csv = convert_df(st.session_state["df"])
        st.download_button(
            "Press to Download",
            csv,
            filename,
            "text/csv",
            key='download-csv'
        )