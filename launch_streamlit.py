import streamlit as st

from src.basic_scrape import basic_scrape
from src.basic_scrappy import basic_scrappy

from main import scrape_city
# Custom functions
from src.sidebar import sidebar


def mainpage():
    st.title("Idealista Web Scrapping")
    initialize() 
    scrape_type_buttons()

def initialize():
    if 'df' not in st.session_state:
        st.session_state['df'] = None


@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

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
    mainpage()
    sidebar()
