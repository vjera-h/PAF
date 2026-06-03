#Koristeći funkcije iz Vježbe 5, za svaki valjak izračunajte
#(a) Srednji radijus R¯ i σR.
#(b) Srednju duljinu L¯ i σL.
#(c) Srednju masu m¯ i σm.
#Ispišite rezultate.

import math

def izracun(brojevi, ime):
    #aritmetička sredina
    n = len(brojevi)
    aritmeticka_sredina = sum(brojevi) / n
    #standardna devijacija
    suma = sum((b - aritmeticka_sredina)**2 for b in brojevi)
    nazivnik = n * (n - 1)
    standardna_devijacija = math.sqrt(suma/nazivnik)

    print(f'Za {ime} {brojevi}:\nAritmetička sredina je: {aritmeticka_sredina}\nStandardna devijacija je: {standardna_devijacija}')

#radijus mm
imer = 'radijus'
D1 = [19.98, 20.18, 20.10, 20.08, 19.74]
D2 = [19.92, 19.82, 19.96, 19.98, 19.88]
D3 = [24.96, 24.98, 24.98, 24.92, 24.94]

R1 = []
R2 = []
R3 = []

def radijus(D, R):
    for d in D:
        r = d/2
        R.append(r)
    return R
radijus(D1, R1)
radijus(D2, R2)
radijus(D3, R3)

izracun(R1, imer)
izracun(R2, imer)
izracun(R3, imer)

#duljina mm
imed = 'duljinu'
L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]

izracun(L1, imed)
izracun(L2, imed)
izracun(L3, imed)

#masa g
imem = 'masu'
m1 = [138.98, 139.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]

izracun(m1, imem)
izracun(m2, imem)
izracun(m3, imem)