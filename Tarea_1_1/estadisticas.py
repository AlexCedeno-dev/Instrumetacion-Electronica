import pandas as pd
import numpy as np

def limpiar_datos(df):
    # Limpia y prepara el DataFrame para análisis estadístico.

    df_limpio = df.copy()

    df_limpio["Voltaje (Volts)"] = pd.to_numeric(
        df_limpio["Voltaje (Volts)"],
        errors="coerce"
    )

    df_limpio = df_limpio.dropna(subset=["Voltaje (Volts)"])

    return df_limpio


def errores_por_hora(df):
    #Calcula error absoluto y relativo por hora.

    df = df.copy()

    df["Error absoluto"] = abs(
        df["Voltaje (Volts)"] - df["Ordenadoascendente"]
    )

    df["Error relativo"] = (
        df["Error absoluto"] / df["Ordenadoascendente"]
    )

    return df


def estadisticas_completas(df):
    #Calcula estadísticas descriptivas completas del voltaje.
    x = df["Voltaje (Volts)"]

    media = x.mean()
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)

    estadisticas = {
        "Media aritmética": media,
        "Mediana": x.median(),
        "Moda": x.mode().iloc[0],
        "Desviación promedio": (x - media).abs().mean(),
        "Desviación estándar": x.std(),
        "Varianza": x.var(),
        "Rango": x.max() - x.min(),
        "Coeficiente de variación": x.std() / media,
        "Semi-intercuartil": (q3 - q1) / 2
    }

    return estadisticas
