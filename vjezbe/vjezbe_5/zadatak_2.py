import numpy as np
import matplotlib.pyplot as plt
from calculus import pravok_aproks, trapezna


def funk(x):
    return x**5 + 4*x + 1 


def analiticki_int(a, b):
    F = lambda x: (1/6)*x**6 + 2*x**2 + x
    return F(b) - F(a)


a = 0
b = 5
br_koraka = [5, 10, 50, 100,150,200,300,500,1000,1500]

analiticko = analiticki_int(a, b)
print('Analitička vrijednost integrala: ',analiticko)



rez_d = []
rez_g = []
rez_trapezna = []

for n in br_koraka:
    donja, gornja = pravok_aproks(funk, a, b, n)
    trap = trapezna(funk, a, b, n)
    rez_d.append(donja)
    rez_g.append(gornja)
    rez_trapezna.append(trap)

plt.figure(figsize=(12, 8))
plt.plot(br_koraka, rez_d, label='Pravokutna metoda (donja suma)', color='green')
plt.plot(br_koraka, rez_g,  label='Pravokutna metoda (gornja suma)', color='purple')
plt.plot(br_koraka, rez_trapezna,label='Trapezna metoda', color='red')
plt.axhline(y=analiticko, color='blue', linestyle='--', label='Analiticka vrijednost')

plt.xlabel('Broj koraka')
plt.ylabel('Vrijednost integrala')
plt.title('Usporedba numeričke i analiticke integracije')
plt.legend()
plt.tight_layout()
plt.show()