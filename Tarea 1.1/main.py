from Datos.lectura_de_datos import leer_datos_pdf

ruta = "Datos/Lecturas_Problema_216.pdf"

df = leer_datos_pdf(ruta)

print(df.head())


from estadisticas import calcular_estadisticas

resultados = calcular_estadisticas(voltajes)

print("Media:", resultados["media"])
print("Desviación estándar:", resultados["desviacion_estandar"])
