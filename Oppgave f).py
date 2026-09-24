import numpy as np
import matplotlib.pyplot as plt

# Leser inn datasettet
data = np.loadtxt("Datasett.dat")

x = data[:, 0]
y = data[:, 1]

# Regresjonslinja fra b)
alpha = 407.0925377084
beta = 2.8746079625

# Lager x-verdier for de to funksjonene
x_plot = np.linspace(min(x), max(x), 500)

# Regresjonslinja
y_reg = alpha + beta*x_plot

# Funksjonen F(x) fra e)
a = 407.045692016344
b = 2.8364515446532534
c = 2.289126141530332
d = 6.197542531946482
f = -0.3253963709691625

F = a + b*x_plot + c*np.sin(d*x_plot + f)

# Plotter datapunktene
plt.scatter(x, y, label="Datapunkter")

# Plotter regresjonslinja
plt.plot(x_plot, y_reg, label="Regresjonslinje")

# Plotter F(x)
plt.plot(x_plot, F, label="F(x)")

plt.xlabel("Tid [år etter 1. januar 2022]")
plt.ylabel("CO$_2$ [ppm]")
plt.title("CO$_2$-data med regresjonslinje og F(x)")
plt.legend()
plt.grid()
plt.show()
