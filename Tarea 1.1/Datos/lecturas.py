import tabula
import pandas as pd

archivo_pdf = "datos/lecturas.pdf"

# Extraer tablas del PDF
tablas = tabula.read_pdf(archivo_pdf, pages="all")

# Unir tablas si hay varias
df = pd.concat(tablas, ignore_index=True)

print(df.head())
