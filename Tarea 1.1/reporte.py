from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_reporte(resultados):
    pdf = canvas.Canvas("Reporte_Instrumentacion.pdf", pagesize=letter)
    y = 750

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Reporte de Análisis de Voltaje")
    y -= 40

    pdf.setFont("Helvetica", 11)
    for clave, valor in resultados.items():
        if not hasattr(valor, "__len__"):
            pdf.drawString(50, y, f"{clave}: {valor:.4f}")
            y -= 20

    pdf.save()
    