import numpy as np
# Importerer NumPy, som brukes til matematiske beregninger

data = np.loadtxt("Datasett.dat")
# Leser inn datasettet fra filen "Datasett.dat"

x = data[:, 0]
# Henter alle x-verdiene fra første kolonne

y = data[:, 1]
# Henter alle y-verdiene fra andre kolonne


def S(a, b, c, d, f):
    # Lager funksjonen S som skal minimeres

    F = a + b*x + c*np.sin(d*x + f)
    # Beregner modellverdiene F(x) for alle x-verdiene

    return np.sum((y - F)**2)
    # Beregner summen av alle de kvadrerte avvikene


a = 407.09
# Bruker alpha fra den lineære regresjonen som startverdi for a

b = 2.87
# Bruker beta fra den lineære regresjonen som startverdi for b

c = 2.0
# Velger en startverdi for amplituden c

d = 2*np.pi
# Velger en startverdi for d

f = 0.0
# Velger en startverdi for faseforskyvningen f


lam = 0.000001
# Setter læringsraten lambda til et lite positivt tall

h = 0.000001
# Setter h til et lite tall for numerisk derivasjon


for n in range(10000):
    # Gjentar gradientmetoden 10000 ganger

    dS_da = (S(a+h, b, c, d, f) - S(a-h, b, c, d, f))/(2*h)
    # Beregner den partielle deriverte til S med hensyn på a

    dS_db = (S(a, b+h, c, d, f) - S(a, b-h, c, d, f))/(2*h)
    # Beregner den partielle deriverte til S med hensyn på b

    dS_dc = (S(a, b, c+h, d, f) - S(a, b, c-h, d, f))/(2*h)
    # Beregner den partielle deriverte til S med hensyn på c

    dS_dd = (S(a, b, c, d+h, f) - S(a, b, c, d-h, f))/(2*h)
    # Beregner den partielle deriverte til S med hensyn på d

    dS_df = (S(a, b, c, d, f+h) - S(a, b, c, d, f-h))/(2*h)
    # Beregner den partielle deriverte til S med hensyn på f


    a = a - lam*dS_da
    # Oppdaterer parameteren a ved å bevege den i retning som reduserer S

    b = b - lam*dS_db
    # Oppdaterer parameteren b

    c = c - lam*dS_dc
    # Oppdaterer parameteren c

    d = d - lam*dS_dd
    # Oppdaterer parameteren d

    f = f - lam*dS_df
    # Oppdaterer parameteren f


print("a =", a)
# Skriver ut den endelige verdien av a

print("b =", b)
# Skriver ut den endelige verdien av b

print("c =", c)
# Skriver ut den endelige verdien av c

print("d =", d)
# Skriver ut den endelige verdien av d

print("f =", f)
# Skriver ut den endelige verdien av f

print("S =", S(a, b, c, d, f))
# Skriver ut den endelige verdien til S
