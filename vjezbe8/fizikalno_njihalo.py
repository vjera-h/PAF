#Fizikalno njihalo ovješeno je pod kutom θ u odnosu na vertikalu. 
# Izmjereni su periodi titranja za dvije duljine njihala, 
# L = 120 mm i L = 240 mm, pri kutovima od 0◦ do 85◦.
import numpy as np
import matplotlib.pyplot as plt


kut_deg = [0 , 5 , 10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50 , 55 , 60 , 65 , 70 , 75 , 80 , 85]

L_1 = 0.12 #m
T_1 = np.array([0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 , 0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 , 2.5460])

L_2 = 0.24 #m
T_2 = np.array([1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 , 1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 , 3.1573])

#Grafički prikažite mjerene podatke i teorijsko predviđanje u grafu ovisnosti perioda o kutu. 

kut = np.radians(kut_deg)

g = 9.81 #m/s^2

#za glatku krivulju
kut_deg_teor = np.linspace(0, 85, 200)
kut_teor = np.radians(kut_deg_teor)

#T(kut) = 2pi * sqrt(l/g cos(kut))
T1_kut = 2 * np.pi * np.sqrt(L_1 /(g * np.cos(kut_teor)))

T2_kut = 2 * np.pi * np.sqrt(L_2/(g * np.cos(kut_teor)))

plt.scatter(kut_deg, T_1, label = 'Mjerenja L1 = 120 mm')
plt.plot(kut_deg_teor, T1_kut, label = 'Teorijsko predviđanje L1')
plt.scatter(kut_deg, T_2, label = 'Mjerenja L2 = 240 mm')
plt.plot(kut_deg_teor, T2_kut, label = 'Teorijsko predviđanje L2')
plt.legend()
plt.grid(True)
plt.show()

# Pomoću curve_fit nađite funkciju koja je rezultat mjerenja te usporedite s 
# funkcijom teorijskog predviđanja. Nađite relativnu pogrešku mjerenja duljine njihala l.
import scipy

