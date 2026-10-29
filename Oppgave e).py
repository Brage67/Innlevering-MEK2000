import numpy as np

# Leser inn datasettet
data = np.loadtxt("Datasett.dat")

x = data[:, 0]
y = data[:, 1]


def S(a, b, c, d, f):
    # Beregner modellverdiene
    F = a + b*x + c*np.sin(d*x + f)

    # Beregner summen av de kvadrerte avvikene
    return np.sum((y - F)**2)


# Startverdier for parameterne
a = 407.09
b = 2.87
c = 2.0
d = 2*np.pi
f = 0.0

# Parametere for gradientmetoden
lam = 0.000001
h = 0.000001
antall_iterasjoner = 10000

print("S før optimalisering =", S(a, b, c, d, f))


# Gradientmetoden
for n in range(antall_iterasjoner):

    # Partielle deriverte
    dS_da = (S(a+h, b, c, d, f) -
             S(a-h, b, c, d, f))/(2*h)

    dS_db = (S(a, b+h, c, d, f) -
             S(a, b-h, c, d, f))/(2*h)

    dS_dc = (S(a, b, c+h, d, f) -
             S(a, b, c-h, d, f))/(2*h)

    dS_dd = (S(a, b, c, d+h, f) -
             S(a, b, c, d-h, f))/(2*h)

    dS_df = (S(a, b, c, d, f+h) -
             S(a, b, c, d, f-h))/(2*h)

    # Oppdaterer alle parameterne
    a = a - lam*dS_da
    b = b - lam*dS_db
    c = c - lam*dS_dc
    d = d - lam*dS_dd
    f = f - lam*dS_df


# Skriver ut resultatene
print("\nResultater etter optimalisering:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("f =", f)

print("S etter optimalisering =", S(a, b, c, d, f))

print(f"F(x) = {a:.6f} + {b:.6f}x + "
      f"{c:.6f}sin({d:.6f}x + {f:.6f})")

