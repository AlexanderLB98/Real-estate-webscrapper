import pandas as pd

def get_number_of_rooms(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["rooms"] = df_new["Detalles"].str.extract(r'(\d+) hab\.')
    return df_new

def get_meters(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["meters"] = df_new["Detalles"].str.extract(r"(\d+) m² ")
    return df_new

def get_elevator(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["Elevator"] = df_new["Detalles"].str.contains("con ascensor", case=False, na=False)
    return df_new

def get_floor(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    # Extrae el número de planta, antes de "ª"
    df_new["Floor"] = df_new["Detalles"].str.extract(r"(\d+)ª")[0]
    return df_new

def fix_price_old(df):
    df_new = df.copy()
    df_new['price'] = df_new["Precio"].str.replace("€", "").str.replace(".", "").str.replace(",", ".").astype(float)
    df_new.drop(columns=["Precio"], inplace=True)
    return df_new

def fix_price(df):
    df_new = df.copy()
    # Remove rows where 'Precio' is not valid (e.g., non-numeric or header text)
    df_new = df_new[df_new["Precio"].str.contains(r"\d", na=False)]  # Keep rows with numbers
    # Clean and convert 'Precio' to a float
    df_new["price"] = (
            df_new["Precio"]
            .str.replace("€", "", regex=False)  # Remove €
            .str.replace(".", "", regex=False)  # Remove thousand separators
            .str.replace(",", ".", regex=False)  # Replace decimal commas with dots
            )
    # Safely convert to numeric and drop invalid rows
    df_new["price"] = pd.to_numeric(df_new["price"], errors="coerce")
    df_new.drop(columns=["Precio"], inplace=True)    
    return df_new

def fix_ID(df):
    df_new = df.copy()
    df_new["ID"] = pd.to_numeric(df_new["ID"], errors='coerce').astype('Int64')
    return df_new

def duplicates_ID(df):
    df_new = df.copy()
    df_new = df_new.drop_duplicates(subset="ID", keep="first")
    return df_new

def apply_pipeline(df: pd.DataFrame, steps: list = [
    fix_ID,
    fix_price,
    get_number_of_rooms,
    get_meters,
    get_elevator,
    get_floor,
    duplicates_ID   
    ] ) -> pd.DataFrame:
    """Apply Feature Engineering to raw dataset, including new attributes
    as numeric price, ID, number of rooms, meters squared, elevator,
    floor...

    Args:
        df (pd.DataFrame): _description_
        steps (list): Pipeline steps to apply

    Returns:
        pd.DataFrame: _description_
    """
    df.dropna(inplace=True)
    for step in steps:
        try:
            df = step(df)
        except Exception as e:
            print("Error in step: " + str(step))
            print(e)
    df.drop(columns=["Detalles"], inplace=True)
    return df
