import numpy as np
import matplotlib.pyplot as plt

# Leser inn datasettet
data = np.loadtxt("Datasett.dat")

# Henter ut x- og y-verdiene
x = data[:, 0]
y = data[:, 1]

# Finner antall datapunkter
n = len(x)

# Beregner summene
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Beregner stigningstallet beta
beta = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

# Beregner konstantleddet alpha
alpha = (sum_y - beta * sum_x) / n

# Beregner regresjonslinjen
y_reg = alpha + beta * x

# Skriver ut resultatene
print("Regresjonsligning:")
print(f"y = {alpha:.4f} + {beta:.4f}x")

# Plotter måledataene
plt.scatter(x, y, label="Måledata")

# Plotter regresjonslinjen
plt.plot(x, y_reg, label="Lineær regresjon")

# Skriver regresjonsligningen på grafen
plt.text(0.2, 421.5, f"y = {alpha:.2f} + {beta:.2f}x")

# Navn på aksene
plt.xlabel("Tid etter 1. januar 2022 [år]")
plt.ylabel("CO2-konsentrasjon [ppm]")

# Viser forklaring og rutenett
plt.legend()
plt.grid(True)

# Viser grafen
plt.show()
