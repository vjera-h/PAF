#Napišite program linregress.py za određivanje modula torzije Dt aluminijske šipke 
# ako znamo da vrijedi M = Dt · φ. Parametri su nam zadani kao 
# M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] Nm,
# φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] rad.
import math
import numpy as np
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #Nm
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #rad



def torzija(M, phi):
    #M = Dt · φ, y = a · x, a = xy/x**2
    n = len(M)

    suma_xy = 0
    suma_x2 = 0
    suma_y2 = 0

    #arit sredine
    for i in range(n):
        suma_xy += M[i] * phi[i]
        suma_x2 += phi[i]**2
        suma_y2 += M[i]**2

    arit_xy = suma_xy/n
    arit_x2 = suma_x2/n
    arit_y2 = suma_y2/n

    Dt = arit_xy/arit_x2

    #standardna devijacija
    stand_dev = np.sqrt((1/n)*(arit_y2/arit_x2 - Dt**2))

    #Dt i standardna devijacija
    print(f'----------------------\nDt = {Dt}, Standardna devijacija = {stand_dev}\n----------------------')

    #za graf
    x_pravac = [0, max(phi)]
    y_pravac = [Dt * x for x in x_pravac]

    plt.scatter(phi, M, label = 'mjerenja', color = 'purple')
    plt.plot(x_pravac, y_pravac, label = 'linearna regresija', color = 'green')
    plt.ylabel('M [Nm]')
    plt.xlabel('$phi$ [rad]')
    plt.legend()
    plt.grid(True)
    plt.show()

torzija(M, phi)