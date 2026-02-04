import numpy as np
import pandas as pd

V_REAL = 127.0

def calcular_estadisticas(voltajes):
    voltajes = pd.Series(voltajes).astype(float)

    media = np.mean(voltajes)
    mediana = np.median(voltajes)
    moda = voltajes.mode()[0]

    error_abs = abs(voltajes - V_REAL)
    error_rel = error_abs / V_REAL

    desv_media = voltajes - media
    desv_prom = np.mean(abs(desv_media))
    desv_std = np.std(voltajes, ddof=1)
    varianza = np.var(voltajes, ddof=1)
    rango = voltajes.max() - voltajes.min()
    coef_var = desv_std / media

    Q1 = np.percentile(voltajes, 25)
    Q3 = np.percentile(voltajes, 75)
    semi_inter = (Q3 - Q1) / 2

    return {
        "media": media,
        "mediana": mediana,
        "moda": moda,
        "error_absoluto": error_abs,
        "error_relativo": error_rel,
        "desviacion_promedio": desv_prom,
        "desviacion_estandar": desv_std,
        "varianza": varianza,
        "rango": rango,
        "coef_variacion": coef_var,
        "semi_intercuartil": semi_inter
    }
