#Libreria
import matplotlib.pyplot as plt

def graficar_voltaje(df):
    #Grafica Voltaje vs Hora.

    plt.figure()
    plt.plot(df["Hora"], df["Voltaje (Volts)"])
    plt.xlabel("Hora")
    plt.ylabel("Voltaje (V)")
    plt.title("Voltaje vs Hora")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def histograma_voltaje(df):
    #Histograma de ocurrencia del voltaje.

    plt.figure()
    plt.hist(df["Voltaje (Volts)"], bins=10)
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma del Voltaje")
    plt.tight_layout()
    plt.show()
