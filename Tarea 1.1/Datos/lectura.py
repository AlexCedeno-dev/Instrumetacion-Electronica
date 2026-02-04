import tabula
import pandas as pd

def leer_datos_pdf(ruta_pdf):
    tablas = tabula.read_pdf(ruta_pdf, pages="all")

    if not tablas:
        raise ValueError("No se encontraron tablas en el PDF")

    df = tablas[0]

    # Limpieza de nombres de columnas
    df.columns = df.columns.str.replace('\r', '', regex=True)

    return df
