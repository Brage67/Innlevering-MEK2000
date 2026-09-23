import numpy as np
# Importerer NumPy, som brukes til å lese og behandle tallene i datasettet

import matplotlib.pyplot as plt
# Importerer pyplot fra Matplotlib, som brukes til å lage grafen

data = np.loadtxt("Datasett.dat")
# Leser tallene fra filen "Datasett.dat" og lagrer dem i variabelen data

x = data[:, 0]
# Henter ut alle verdiene i den første kolonnen som x-verdier

y = data[:, 1]
# Henter ut alle verdiene i den andre kolonnen som y-verdier

plt.scatter(x, y)
# Lager et punktdiagram med x-verdiene på x-aksen og y-verdiene på y-aksen

plt.xlabel("Tid etter 1. januar 2022 [år]")
# Gir x-aksen navn og angir at tiden er målt i år

plt.ylabel("CO₂-konsentrasjon [ppm]")
# Gir y-aksen navn og angir at CO₂-konsentrasjonen måles i ppm

plt.show()
# Viser grafen på skjermen
