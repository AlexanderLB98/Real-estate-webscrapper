import streamlit as st
import os

from src.basic_scrape import basic_scrape
from src.basic_scrappy import basic_scrappy

from src.utils import convert_df

from src.streamlit_src import data_cleaning_pipeline
from main import scrape_city

# Custom functions
from src.sidebar import sidebar

def mainpage(selected_files):
    st.title("Idealista Web Scrapping")
    initialize() 
    scrape_type_buttons()
    data_cleaning_pipeline(selected_files)

def initialize():
    if 'df' not in st.session_state:
        st.session_state['df'] = None

def scrape_type_buttons():
    city = st.text_input("Write city")
    if st.button("Scrape data"):
        st.session_state["df"] = scrape_city(city) 
        st.write(st.session_state["df"])
        #     st.download_button("Download scrapped data", df, file_name="scrapped_data_" + city + ".csv")
        csv = convert_df(st.session_state["df"])
        st.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
        )

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    selected_files = sidebar()
    mainpage(selected_files)
    
