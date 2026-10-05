import numpy as np
import matplotlib.pyplot as plt

# Parameterne fra e)
a = 407.045692016344
b = 2.8364515446532534
c = 2.289126141530332
d = 6.197542531946482
f = -0.3253963709691625

# Modellfunksjonen
def F(x):
    return a + b*x + c*np.sin(d*x + f)

# Lager x-verdier gjennom hele 2027
x_2027 = np.linspace(5, 6, 500)

# Beregner F(x) for 2027
F_2027 = F(x_2027)

# Beregner forventet CO2-konsentrasjon ved nyttår 2027
CO2_nyttaar = F(5)

print("Forventet CO2-konsentrasjon ved nyttår 2027:",
      CO2_nyttaar, "ppm")

# Plotter modellen
plt.plot(x_2027, F_2027, label="F(x)")

# Marker verdien ved nyttår 2027
plt.plot(5, CO2_nyttaar, 'o', label="1. januar 2027")

plt.xlabel("Tid [år etter 1. januar 2022]")
plt.ylabel("CO$_2$ [ppm]")
plt.title("Forventet CO$_2$-konsentrasjon i 2027")
plt.legend()
plt.grid()
plt.show()
