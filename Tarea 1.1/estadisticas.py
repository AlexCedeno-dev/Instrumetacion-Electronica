# ==========================================
# CÁLCULOS ESTADÍSTICOS
# Archivo: estadisticas.py
# ==========================================

import numpy as np
import pandas as pd

# Voltaje real del sistema
V_REAL = 127.0


def calcular_estadisticas(voltajes):
    """
    Calcula las estadísticas descriptivas solicitadas
    para un conjunto de lecturas de voltaje.

    Parámetros:
        voltajes (Series o lista): lecturas de voltaje

    Retorna:
        resultados (dict): diccionario con estadísticas
    """

    # Asegurar que los datos sean numéricos
    voltajes = pd.Series(voltajes).astype(float)

    # ---- MEDIDAS DE TENDENCIA CENTRAL ----
    media = np.mean(voltajes)
    mediana = np.median(voltajes)
    moda = voltajes.mode()[0]

    # ---- ERRORES ----
    error_absoluto = abs(voltajes - V_REAL)
    error_relativo = error_absoluto / V_REAL

    # ---- DESVIACIONES ----
    desviacion_media = voltajes - media
    desviacion_promedio = np.mean(abs(desviacion_media))

    # ---- DISPERSIÓN ----
    desviacion_estandar = np.std(voltajes, ddof=1)
    varianza = np.var(voltajes, ddof=1)
    rango = voltajes.max() - voltajes.min()
    coef_variacion = desviacion_estandar / media

    # ---- CUARTILES ----
    Q1 = np.percentile(voltajes, 25)
    Q3 = np.percentile(voltajes, 75)
    semi_intercuartil = (Q3 - Q1) / 2

    # Guardar todos los resultados en un diccionario
    resultados = {
        "media": media,
        "mediana": mediana,
        "moda": moda,
        "error_absoluto": error_absoluto,
        "error_relativo": error_relativo,
        "desviacion_media": desviacion_media,
        "desviacion_promedio": desviacion_promedio,
        "desviacion_estandar": desviacion_estandar,
        "varianza": varianza,
        "rango": rango,
        "coef_variacion": coef_variacion,
        "semi_intercuartil": semi_intercuartil
    }

    return resultados
