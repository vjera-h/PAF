#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, 
# a program crta x − t, v − t i a − t graf za prvih 10 sekundi jednolikog 
# gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte numerički. 
# Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        F = float(input('Unesite iznos sile u N: ')) #unos sile N
        m = float(input('Unesite masu čestice u kg: ')) #unos mase kg
        break
    except ValueError:
        print('Potrebno je upisati broj')

t = np.linspace(0, 11, 100) #vrijeme od 0 do 10 sekundi

a = F / m #akceleracija F = m*a
atr = np.linspace(a, a, 100)
x = 0.5 * a * t**2 #položaj x - x0 = v0*t + 0.5*a*t^2, x0 = 0, v0 = 0
v = a * t #brzina v - v0 = a*t, v0 = 0

#graf za položaj
plt.figure(figsize=(6,10))
plt.plot(t, x, color = 'pink') 
plt.title('x - t graf')
plt.xlabel('t (s)')
plt.ylabel('x (m)')  
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid()
plt.show()

#graf za brzinu
plt.figure(figsize=(6,10))
plt.plot(t, v, color = 'purple') 
plt.title('v - t graf')
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')  
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid()
plt.show()

#graf za akceleraciju
plt.figure(figsize=(6,10))
plt.plot(t, atr, color = 'blue') 
plt.title('a - t graf')
plt.xlabel('t (s)')
plt.ylabel('a (m/s^2)')  
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid()
plt.show()


