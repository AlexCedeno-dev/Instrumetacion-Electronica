# LECTURA DE DATOS DESDE PDF
import tabula           # Para extraer tablas desde PDF
import pandas as pd     # Para manejar los datos como tablas


def leer_datos_pdf(ruta_pdf):
    """
    Lee un archivo PDF que contiene lecturas de voltaje
    y regresa un DataFrame con las columnas necesarias.
    
    Parámetros:
        ruta_pdf (str): Ruta del archivo PDF
    
    Retorna:
        df (DataFrame): Tabla con las lecturas de voltaje
    """

    # Extraer todas las tablas del PDF
    tablas = tabula.read_pdf(ruta_pdf, pages="all")

    # Unir todas las tablas en una sola
    df = pd.concat(tablas, ignore_index=True)

    # Mostrar columnas encontradas (útil para depuración)
    print("Columnas encontradas en el PDF:")
    print(df.columns)

    # Limpieza básica:
    # Eliminar filas vacías
    df = df.dropna(how="all")

    return df
