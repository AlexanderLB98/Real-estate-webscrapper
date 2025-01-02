import pandas as pd
import numpy as np
import os

# Ruta del directorio
base_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta de los archivos
input_path = os.path.join(base_dir, 'data', 'raw', 'scraped_data-barcelona.csv')
output_dir = os.path.join(base_dir, 'data', 'processed')
output_path = os.path.join(output_dir, 'cleaned_data-barcelona.csv')

data = pd.read_csv(input_path, header=0)


# Eliminar filas con valores nulos en las columnas ID o Precio
data = data.dropna(subset=['ID', 'Precio'])

# Eliminamos filas donde el precio es 0.
data = data[data['Precio'] != 0]

# Se filtran las filas donde 'ID' no es convertible a número
data = data[pd.to_numeric(data['ID'], errors='coerce').notnull()]

# 'ID' a entero
data['ID'] = data['ID'].astype(int)

# Reemplazar valores nulos, ceros y vacíos por NaN en la resta de columnas
columns_to_check = ['Título', 'Enlace', 'Detalles', 'Descripción']
for column in columns_to_check:
    data[column] = data[column].replace([0, '', np.nan], np.nan)

# Eliminar filas duplicadas en 'ID'
data = data.drop_duplicates(subset=['ID'])

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Guardar el archivo procesado
data.to_csv(output_path, index=False)

# DataFrame después de la limpieza
print("Datos después de la limpieza:")
print(data.head())
