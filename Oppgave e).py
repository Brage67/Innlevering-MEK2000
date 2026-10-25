
import numpy as np
# Importerer NumPy, som brukes til matematiske beregninger

data = np.loadtxt("Datasett.dat")
# Leser inn datasettet fra filen "Datasett.dat"

x = data[:, 0]
# Henter alle x-verdiene fra første kolonne

y = data[:, 1]
# Henter alle y-verdiene fra andre kolonne


def S(a, b, c, d, f):
    # Definerer funksjonen som skal minimeres

    F = a + b*x + c*np.sin(d*x + f)
    # Beregner modellverdiene for alle datapunktene

    return np.sum((y - F)**2)
    # Beregner summen av de kvadrerte avvikene


# Startverdier for parameterne
a = 407.09
b = 2.87
c = 2.0
d = 2*np.pi
f = 0.0

# Parametere for gradientmetoden
lam = 0.000001
h = 0.000001
antall_iterasjoner = 100000

# Skriver ut startverdien til S
print("S før optimalisering =", S(a, b, c, d, f))


for n in range(antall_iterasjoner):

    # Beregner de partielle deriverte numerisk
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

    # Oppdaterer parameterne ved hjelp av gradientmetoden
    a = a - lam*dS_da
    b = b - lam*dS_db
   
