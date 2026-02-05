from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import PageBreak



def generar_reporte(df, estadisticas):
    # Crear documento PDF
    doc = SimpleDocTemplate("Reporte de Monitoreo de Voltaje del Regulador.pdf")

    estilos = getSampleStyleSheet()
    elementos = []

    # ----------------- TÍTULO -----------------
    elementos.append(Paragraph(
        "Reporte de Monitoreo de Voltaje del Regulador",
        estilos["Title"]
    ))
    elementos.append(Spacer(1, 20))

    # ----------------- TABLA DE DATOS -----------------
    elementos.append(Paragraph(
        "Datos de las Mediciones (muestra representativa)",
        estilos["Heading2"]
    ))
    elementos.append(Spacer(1, 20))

    tabla_datos = [
        ["Hora", "Voltaje (V)", "Error absoluto (V)", "Error relativo"]
    ]

    # Mostrar solo las primeras 10 mediciones
    for _, fila in df.iterrows():
        tabla_datos.append([
            fila["Hora"],
            f"{fila['Voltaje (Volts)']:.2f}",
            f"{fila['Error absoluto']:.4f}",
            f"{fila['Error relativo']:.4f}"
        ])

    tabla = Table(tabla_datos, colWidths=[80, 100, 120, 120])

    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 20))
    elementos.append(PageBreak())

    # ----------------- ESTADÍSTICAS -----------------
    elementos.append(Paragraph(
        "Resultados Estadísticos",
        estilos["Heading2"]
    ))
    elementos.append(Spacer(1, 12))

    for clave, valor in estadisticas.items():
        texto = f"{clave}: {valor:.4f}"
        elementos.append(Paragraph(texto, estilos["Normal"]))

    elementos.append(Spacer(1, 20))
    elementos.append(PageBreak())

    # ----------------- GRÁFICAS -----------------
    elementos.append(Paragraph(
        "Gráficas",
        estilos["Heading2"]
    ))
    elementos.append(Spacer(1, 12))

    # Gráfica Voltaje vs Hora
    elementos.append(Paragraph("Voltaje vs Hora", estilos["Normal"]))
    elementos.append(Spacer(1, 8))
    elementos.append(Image("voltaje_vs_hora.png", width=400, height=200))

    elementos.append(Spacer(1, 20))

    # Histograma
    elementos.append(Paragraph("Histograma del Voltaje", estilos["Normal"]))
    elementos.append(Spacer(1, 8))
    elementos.append(Image("histograma_voltaje.png", width=400, height=200))

    # ----------------- GENERAR PDF -----------------
    doc.build(elementos)

    print("PDF generado correctamente: Tarea1.1_Resultados.pdf")
