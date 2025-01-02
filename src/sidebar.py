import streamlit as st
import os

def sidebar():
    """
    Set different options
    """
    st.sidebar.title("Sidebar")

    st.sidebar.header("Load data")
    
    selected_files = select_csv_files()
    ### User Agent

    ### IP Rotation

    ### Cookies management
    
    return selected_files

def select_csv_files():
    raw_path = "data/raw/"
    csv_files = [file for file in os.listdir(raw_path) if file.endswith(".csv")]
    
    # Lista para almacenar los archivos seleccionados
    selected_files = []

    # Itera por cada archivo y crea un checkbox
    st.sidebar.write("Archivos disponibles:")
    for file in csv_files:
        if st.sidebar.checkbox(file, key=file, value=True):
            selected_files.append(file)
    return selected_files
