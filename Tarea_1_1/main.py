from datos.lectura import leer_pdf
from estadisticas import limpiar_datos, errores_por_hora, estadisticas_completas
from graficas import graficar_voltaje, histograma_voltaje
from reporte import generar_reporte

df = leer_pdf("datos/PRUEBA DE PROGRAMA EJ2025.pdf")
df = limpiar_datos(df)

df = errores_por_hora(df)
estadisticas = estadisticas_completas(df)

# Gráficas 
graficar_voltaje(df)
histograma_voltaje(df)

# PDF SOLO CON RESULTADOS
generar_reporte(df, estadisticas)
