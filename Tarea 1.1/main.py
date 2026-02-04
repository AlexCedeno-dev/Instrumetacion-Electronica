from Datos.lectura_de_datos import leer_datos_pdf
from estadisticas import calcular_estadisticas
from graficas import grafica_voltaje_tiempo, histograma_voltajes
from reporte import generar_reporte

# Leer datos
ruta_pdf = "Datos/Lecturas_Problema_216.pdf"
df = leer_datos_pdf(ruta_pdf)

# Extraer columna de voltaje (ajusta el nombre si es necesario)
voltajes = df["Voltaje (Volts)"]

# Estadísticas
resultados = calcular_estadisticas(voltajes)

# Gráficas
grafica_voltaje_tiempo(voltajes)
histograma_voltajes(voltajes)

# Reporte
generar_reporte(resultados)
