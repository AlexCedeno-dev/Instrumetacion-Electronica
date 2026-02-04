from Datos.lectura_de_datos import leer_datos_pdf
from estadisticas import calcular_estadisticas
from graficas import grafica_voltaje, histograma
from reporte import generar_reporte

ruta_pdf = "datos/Lecturas.pdf"

df = leer_datos_pdf(ruta_pdf)

print(df.columns)  # para ver columnas reales

# Ajusta el índice si el nombre cambia
voltajes = df.iloc[:, 2]

resultados = calcular_estadisticas(voltajes)

grafica_voltaje(voltajes)
histograma(voltajes)

generar_reporte(resultados)
