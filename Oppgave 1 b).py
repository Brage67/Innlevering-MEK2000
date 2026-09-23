import numpy as np
# Importerer NumPy, som brukes til å arbeide med tall og datasettet

import matplotlib.pyplot as plt
# Importerer Matplotlib, som brukes til å lage grafen

data = np.loadtxt("Datasett.dat")
# Leser inn datasettet fra filen "Datasett.dat"

x = data[:, 0]
# Henter alle verdiene i første kolonne som x-verdier

y = data[:, 1]
# Henter alle verdiene i andre kolonne som y-verdier

beta, alpha = np.polyfit(x, y, 1)
# Finner stigningstallet beta og konstantleddet alpha for regresjonslinjen
# Tallet 1 betyr at vi bruker en lineær regresjon

y_reg = alpha + beta*x
# Beregner y-verdiene til regresjonslinjen

print("Regresjonsligning:")
# Skriver ut en overskrift for regresjonsligningen

print(f"y = {alpha:.2f} + {beta:.2f}x")
# Skriver ut regresjonsligningen med to desimaler

plt.scatter(x, y)
# Plotter måledataene som separate punkter

plt.plot(x, y_reg)
# Plotter regresjonslinjen sammen med måledataene

plt.text(0.2, 421.5, f"y = {alpha:.2f} + {beta:.2f}x")
# Skriver regresjonsligningen inn på grafen

plt.xlabel("Tid etter 1. januar 2022 [år]")
# Gir x-aksen navn og angir enheten

plt.ylabel("CO₂-konsentrasjon [ppm]")
# Gir y-aksen navn og angir enheten

plt.show()
# Viser grafen
