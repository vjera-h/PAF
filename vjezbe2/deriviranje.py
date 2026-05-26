# Testirajte modul na primjerima kubne i trigonometrijske funkcije. 
# Neka korisnik u svom kodu importa modul calculus i za derivaciju koristi gotove metode iz 
# tog modula. Nacrtajte na istom grafu analitičko rješenje i numerička rješenja za 
# različite korake numeričke derivacije. To ćete postići tako da u razvijenim metodama iz 
# modula calculus dodate opciju da metoda kao jedan od ulaznih parametara prima i veličinu
# koraka derivacije ϵ i metodu kojom derivira. Neka "three-step" metoda bude zadana ako 
# korisnik ništa ne odabere, a "two-step" metoda bude druga ponuđena opcija.

import calculus
import numpy as np
import matplotlib.pyplot as plt

#kubna funkcija numericka f(x) = x^3 - 3x^2 + 2x, analiticka f'(x) = 3x^2 - 6x + 2
def kubna_numericka(x):
    return x**3 - 3*x**2 + 2*x
def kubna_analiticka(x):
    return 3*x**2 - 6*x + 2

#trigonometrijska funkcija numericka f(x) = sin(x), analiticka f'(x) = cos(x)
def trig_numericka(x):
    return np.sin(x)
def trig_analiticka(x):
    return np.cos(x)

print('Upišite potrebno:\n')
x_min = float(input('Upisite x minimum: '))
x_max = float(input('Upisite x maksimum: '))
epsilon = float(input('Upisite korak (npr. 0.5, 0.1): '))
#za crtanje analitickog rjesenja
x_ana = np.linspace(x_min, x_max, 500)

#radi dva podgrafa
fig, (ax1, ax2) = plt.subplots(1, 2) #jedan red dva stupca

#numeričko rješenje
x1, y1_three = calculus.derivacija_raspon(kubna_numericka, x_min, x_max, epsilon = epsilon, metoda = 'three step')
_,  y1_two   = calculus.derivacija_raspon(kubna_numericka, x_min, x_max, epsilon = epsilon, metoda = 'two step')

x2, y2_three = calculus.derivacija_raspon(trig_numericka, x_min, x_max, epsilon = epsilon, metoda = 'three step')
_,  y2_two   = calculus.derivacija_raspon(trig_numericka, x_min, x_max, epsilon = epsilon, metoda = 'two step')

#analitičko rješenje
y_ana1 = kubna_analiticka(x1)
y_ana2 = trig_analiticka(x2)

plt.figure(figsize=(12,12))

#kubna x^3
plt.subplot(2,1,1)
plt.plot(x1, y_ana1, color = 'blue', linewidth = 2, label = 'Analitičko rješenje')
plt.plot(x1, y1_three, color = 'cyan', label = 'Three step - numeričko rješenje')
plt.plot(x1, y1_two, color = 'green', label = 'Two step - numeričko rješenje')
plt.title('Derivacija kubne funkcije')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid(True)

#trigonometrijska sin(x)
plt.subplot(2,1,2)
plt.plot(x2, y_ana2, color = 'red', linewidth = 2, label = 'Analitičko rješenje')
plt.plot(x2, y2_three, '--', color = 'yellow', label = 'Three step - numeričko rješenje')
plt.plot(x2, y2_two, ':', color = 'orange', label = 'Two step - numeričko rješenje')
plt.title('Derivacija trigonometrijske funkcije')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid(True)

plt.show()