import matplotlib.pyplot as plt

V_REAL = 127.0
LIM_SUP = V_REAL * 1.03
LIM_INF = V_REAL * 0.97

def grafica_voltaje(voltajes):
    plt.figure()
    plt.plot(voltajes, marker='o', label="Voltaje medido")
    plt.axhline(V_REAL, linestyle='--', label="127 V")
    plt.axhline(LIM_SUP, linestyle=':', label="+3%")
    plt.axhline(LIM_INF, linestyle=':', label="-3%")
    plt.xlabel("Muestra")
    plt.ylabel("Voltaje (V)")
    plt.title("Voltaje vs Tiempo")
    plt.legend()
    plt.grid()
    plt.show()

def histograma(voltajes):
    plt.figure()
    plt.hist(voltajes, bins=10)
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de Voltajes")
    plt.grid()
    plt.show()
