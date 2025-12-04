"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    csv_path = "files/input/news.csv"
    df = pd.read_csv(csv_path, index_col=0)

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["Television"], marker="o", label="Television")
    plt.plot(df.index, df["Newspaper"], marker="o", label="Newspaper")
    plt.plot(df.index, df["Internet"], marker="o", label="Internet")
    plt.plot(df.index, df["Radio"], marker="o", label="Radio")

    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("News Source Trends Over Time")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(df.index, rotation=45)

    os.makedirs("files/plots", exist_ok=True)

    plt.savefig("files/plots/news.png", dpi=300, bbox_inches="tight")
    plt.close()
