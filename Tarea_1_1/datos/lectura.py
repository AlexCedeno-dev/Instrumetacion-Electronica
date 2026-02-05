#Librerias
import tabula  
import pandas as pd

def leer_pdf(ruta_pdf):
    tablas = tabula.read_pdf(ruta_pdf, pages="all")

    if not tablas:
        raise ValueError("No se encontraron tablas en el PDF")

    df = tablas[0]

    # Limpiar nombres de columnas (saltos raros del PDF)
    df.columns = df.columns.str.replace('\r', '', regex=True)

    return df
