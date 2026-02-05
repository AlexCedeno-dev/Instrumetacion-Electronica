#Librerias
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors

def generar_reporte(df, estadisticas):
    archivo = "Reporte de Resultados.pdf"

    doc = SimpleDocTemplate(archivo, pagesize=LETTER)
    estilos = getSampleStyleSheet()
    contenido = []

    # ===== PORTADA =====
    contenido.append(Paragraph("<b>Tarea 1.1 – Resultados</b>", estilos["Title"]))
    contenido.append(Spacer(1, 20))

    # ===== TABLA DE ERRORES =====
    contenido.append(Paragraph("<b>Error absoluto y relativo por hora</b>", estilos["Heading2"]))
    contenido.append(Spacer(1, 10))

    tabla_datos = [
        ["Hora", "Error absoluto", "Error relativo"]
    ]

    for _, fila in df.iterrows():
        tabla_datos.append([
            str(fila["Hora"]),
            f"{fila['Error absoluto']:.4f}",
            f"{fila['Error relativo']:.4f}"
        ])

    tabla = Table(tabla_datos, repeatRows=1)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),

    ]))

    contenido.append(tabla)
    contenido.append(Spacer(1, 25))

    # ===== ESTADÍSTICOS =====
    contenido.append(Paragraph("<b>Resultados estadísticos</b>", estilos["Heading2"]))
    contenido.append(Spacer(1, 10))

    for clave, valor in estadisticas.items():
        contenido.append(Paragraph(
            f"{clave}: {valor:.4f}",
            estilos["Normal"]
        ))

    doc.build(contenido)

    print(f"PDF generado correctamente: {archivo}")
