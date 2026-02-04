    # ==========================================
# GENERACIÓN DE REPORTE PDF
# Archivo: reporte.py
# ==========================================

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date

V_REAL = 127.0


def generar_reporte(resultados, nombre_archivo="Reporte_Instrumentacion.pdf"):
    """
    Genera un reporte en PDF con los resultados estadísticos.

    Parámetros:
        resultados (dict): diccionario con estadísticas calculadas
        nombre_archivo (str): nombre del archivo PDF a generar
    """

    # Crear el PDF
    pdf = canvas.Canvas(nombre_archivo, pagesize=letter)
    ancho, alto = letter

    # Fecha actual
    fecha = date.today().strftime("%d/%m/%Y")

    # ---- TÍTULO ----
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(ancho / 2, alto - 50, "REPORTE DE ANÁLISIS DE VOLTAJE")

    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(ancho / 2, alto - 70, f"Fecha: {fecha}")
    pdf.drawCentredString(ancho / 2, alto - 85, "Sistema de Instrumentación Electrónica")

    # ---- CONTENIDO ----
    y = alto - 130
    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, y, f"Voltaje nominal del sistema: {V_REAL} V")
    y -= 30

    pdf.drawString(50, y, f"Media: {resultados['media']:.2f} V")
    y -= 20

    pdf.drawString(50, y, f"Mediana: {resultados['mediana']:.2f} V")
    y -= 20

    pdf.drawString(50, y, f"Moda: {resultados['moda']:.2f} V")
    y -= 20

    pdf.drawString(50, y, f"Desviación estándar: {resultados['desviacion_estandar']:.2f} V")
    y -= 20

    pdf.drawString(50, y, f"Varianza: {resultados['varianza']:.2f}")
    y -= 20

    pdf.drawString(50, y, f"Rango: {resultados['rango']:.2f} V")
    y -= 20

    pdf.drawString(50, y, f"Coeficiente de variación: {resultados['coef_variacion']:.4f}")
    y -= 20

    pdf.drawString(50, y, f"Semi-intercuartil: {resultados['semi_intercuartil']:.2f} V")

    # ---- PIE DE PÁGINA ----
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawString(50, 40, "Reporte generado automáticamente con Python.")

    # Guardar archivo
    pdf.save()

    print("Reporte PDF generado correctamente.")
