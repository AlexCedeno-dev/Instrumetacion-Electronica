from datos.lectura import leer_pdf

RUTA_PDF = "datos/lecturas.pdf"

df = leer_pdf(RUTA_PDF)

print(df.head())
print(df.columns)
