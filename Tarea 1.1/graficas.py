# ==========================================
# GRÁFICAS DEL SISTEMA DE VOLTAJE
# Archivo: graficas.py
# ==========================================

import matplotlib.pyplot as plt
import numpy as np

# Voltaje nominal
V_REAL = 127.0

# Límites permitidos ±3%
LIMITE_SUP = V_REAL * 1.03
LIMITE_INF = V_REAL * 0.97


def grafica_voltaje_tiempo(voltajes):
    """
    Genera la gráfica Voltaje vs Tiempo (muestras)

    Parámetros:
        voltajes (Series o lista): lecturas de voltaje
    """

    plt.figure()
    plt.plot(voltajes, marker='o', label="Voltaje medido")

    # Líneas de referencia
    plt.axhline(V_REAL, linestyle='--', label="Voltaje nominal (127 V)")
    plt.axhline(LIMITE_SUP, linestyle=':', label="Límite superior +3%")
    plt.axhline(LIMITE_INF, linestyle=':', label="Límite inferior -3%")

    plt.title("Voltaje vs Tiempo")
    plt.xlabel("Muestra (cada 30 min)")
    plt.ylabel("Voltaje (V)")
    plt.legend()
    plt.grid()
    plt.show()


def histograma_voltajes(voltajes):
    """
    Genera el histograma de ocurrencia de las muestras

    Parámetros:
        voltajes (Series o lista): lecturas de voltaje
    """

    plt.figure()
    plt.hist(voltajes, bins=10)

    plt.title("Histograma de Voltajes")
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.grid()
    plt.show()
