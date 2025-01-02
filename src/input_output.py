import pandas as pd
import os

def load_data(raw_path = "data/raw/", files=None):
    if files is None:
        files = [file for file in os.listdir(raw_path) if file.endswith(".csv")]
    
    df = pd.DataFrame()
    for file in files:
        city = file.split("scraped_data-")[1].split(".csv")[0]
        temp_df = pd.read_csv(os.path.join(raw_path, file))
        temp_df["city"] = city
        df = pd.concat([df, temp_df], ignore_index=True)
    return df