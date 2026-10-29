
import numpy as np
import matplotlib.pyplot as plt

# Leser inn datasettet
data = np.loadtxt("Datasett.dat")

x = data[:, 0]
y = data[:, 1]

# Lineær regresjon fra oppgave b)
alpha = 407.0925377084
beta = 2.8746079625

# Parametere fra oppgave e)
a = 407.045692016344
b = 2.8364515446532534
c = 2.289126141530332
d = 6.197542531946482
f = -0.3253963709691625

# Lager x-verdier for å tegne glatte kurver
x_plot = np.linspace(min(x), max(x), 500)

# Beregner den lineære regresjonslinjen
y_reg = alpha + beta*x_plot

# Beregner den sinusformede modellen
F = a + b*x_plot + c*np.sin(d*x_plot + f)

# Tegner måledataene
plt.scatter(x, y, label="Måledata")

# Tegner regresjonslinjen
plt.plot(x_plot, y_reg, label="Lineær regresjon")

# Tegner den sinusformede modellen
plt.plot(x_plot, F, label="Sinusformet modell")

# Setter navn på aksene
plt.xlabel("Tid etter 1. januar 2022 [år]")
plt.ylabel("CO2-konsentrasjon [ppm]")

# Viser tegnforklaring og rutenett
plt.legend()
plt.grid(True)

# Viser figuren
plt.show()


