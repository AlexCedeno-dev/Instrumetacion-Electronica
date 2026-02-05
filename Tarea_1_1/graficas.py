import matplotlib.pyplot as plt

def graficar_voltaje(df):
    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Hora"],
        df["Voltaje (Volts)"],
        linewidth=2,
        marker="o",
        markersize=4,
        label="Voltaje medido"
    )

    plt.axhline(
        y=127,
        linestyle="--",
        linewidth=2,
        label="Voltaje nominal (127 V)"
    )

    plt.title("Voltaje del regulador vs Hora")
    plt.xlabel("Hora")
    plt.ylabel("Voltaje (V)")
    plt.xticks(df["Hora"][::4], rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # 🔥 GUARDAR IMAGEN
    plt.savefig("voltaje_vs_hora.png", dpi=300)
    plt.close()


def histograma_voltaje(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["Voltaje (Volts)"], bins=10)
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma del voltaje")
    plt.tight_layout()

    # 🔥 GUARDAR IMAGEN
    plt.savefig("histograma_voltaje.png", dpi=300)
    plt.close()
