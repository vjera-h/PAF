# Napišite program arithm.py koji računa aritmetičku sredinu i 
# standardnu devijaciju za 10 točaka.
import math 

brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def izračun(brojevi):
    #aritmetička sredina
    n = len(brojevi)
    aritmeticka_sredina = sum(brojevi) / n
    #standardna devijacija
    suma = sum((b - aritmeticka_sredina)**2 for b in brojevi)
    nazivnik = n * (n - 1)
    standardna_devijacija = math.sqrt(suma/nazivnik)

    print(f'Aritmetička sredina je: {aritmeticka_sredina}\nStandardna devijacija je: {standardna_devijacija}')

izračun(brojevi)