#Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije. 
# Neka korisnik u svom kodu importa modul calculus i za integraciju koristi 
# gotove metode iz tog modula. Nacrtajte na istom grafu analitičko riješenje i 
# numerička riješenja za različiti broj koraka i obe metode numeričke integracije.

import calculus
import numpy as np
import matplotlib.pyplot as plt

def funkcija(x):
    return x**2

a = 2
b = 3

n_broj = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

lijeva = [] #prazne liste za rezultate lijeve i desne strane pravokutne aproksimacije
desna = []
trapezna = []

#numericko
for n in n_broj:
    l, d = calculus.pravokutna_aproksimacija(funkcija, a, b, n)
    lijeva.append(l)
    desna.append(d)
    trapezna.append(calculus.trapezna_aproksimacija(funkcija, a, b, n))

#analiticko - trapezna
suma_ana = calculus.trapezna_aproksimacija(funkcija, a, b, 10000)


plt.scatter(n_broj, lijeva, color = 'blue', linewidth = 5, label = 'Pravokutna lijeva aproksimacija')
plt.scatter(n_broj, desna, color = 'cyan', linewidth = 1, label = 'Pravokutna desna aproksimacija')
plt.scatter(n_broj, trapezna, color = 'green', label = 'Trapezna aproksimacija')
plt.title('Integriranje')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()
plt.axhline(suma_ana, color = 'black', label = 'Analiticko rjesenje')
plt.grid(True)
plt.show()