#U pokusu s diskom, disk slobodno pada dok odmata nit s osovine polumjera r. 
# Izmjereni su prosječni padovi h (mjereni od dna) i odgovarajuća srednja vremena pada t. 
# Ukupna visina iznosi h0 = 0.54 m, masa diska m = 525.7 g, polumjer osovine r = 4.025 mm.
import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54 # m 
m = 0.5257 # kg
r = 4.025e-3 # m
g = 9.81 #m/s^2

h = np.array([0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40]) # m
t_mean = np.array([1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813]) # s

# (a) Linearizacijom prema jednadžbi (5) napravite prikaz log(s)- log(t) 
# i odredite nagib i odsječak. Nacrtajte točke mjerenja i odgovarajući pravac. 
# Ispišite rezultate za parametre a i b te njihove pogreške.

#log(s) = 2log(t) + log(a_ef/2), y = ax + b
#y = log(s), x = log(t), a = 2, b = log(a_ef/2)
s = h0 - h

y = np.log(s)
x = np.log(t_mean)



n = len(h) #broj tocaka

a = (n * np.sum(x * y) - np.sum(x) * np.sum(y))/(n * np.sum(x**2) - (np.sum(x))**2) #formula (1) nagib

b = (np.sum(y) - (a * np.sum(x)))/n #formula (2) odsječak

x_pravac = x 
y_pravac = a * x + b  #formula (5)

#standardna devijacija a i b za y = ax + b po dodatku c iz "Praktikum iz mehanike"
sr_y2 = np.mean(y**2)
sr_y = np.mean(y)
sr_x2 = np.mean(x**2)
sr_x = np.mean(x)
devi_a = np.sqrt((1/n)*((sr_y2 - sr_y**2)/(sr_x2 - sr_x**2) - a**2))
devi_b = devi_a * np.sqrt(sr_x2 - sr_x**2)

#log(a_ef/2) = log(s) - 2log(t) = b
a_ef_a = 2 * np.exp(b)
devi_a_ef_a = a_ef_a * devi_b

print('-'*50)
print(f'log(s) - log(t)\na = {a:.4f} +- {devi_a:.4f}\nb = {b:.4f} +- {devi_b:.4f}')

plt.scatter(x, y, color = 'blue', label = 'Mjerenja')
plt.plot(x_pravac, y_pravac, color = 'cyan', label = 'Linearizacija')
plt.title('log(s) - log(t) graf')
plt.xlabel('log(t)')
plt.ylabel('log(s)')
plt.legend()
plt.grid(True)
plt.show()

#(b) Napravite isto kao i u prethodnom koraku za prikaz s − t^2 grafa.
#s = 1/2 * a_ef * t^2, y = ax +b
#y = s, a = 1/2 * a_ef, x = t^2, b = 0
xb = t_mean**2
yb = s

ab = np.sum(xb * yb)/np.sum(xb**2)

xb_pravac = xb
yb_pravac = ab * xb

#standardna devijacija a za y = ax po dodatku c iz "Praktikum iz mehanike"
sr_yb2 = np.mean(yb**2)
sr_xb2 = np.mean(xb**2)
devi_ab = np.sqrt((1/n)*((sr_yb2/sr_xb2) - ab**2))

a_ef_b = 2 * ab
devi_a_ef_b = 2 * devi_ab

print('-'*50)
print(f's - t^2\na = {ab:.4f} +- {devi_ab:.4f}')

plt.scatter(xb, yb, color = 'blue', label = 'Mjerenja')
plt.plot(xb_pravac, yb_pravac, color = 'cyan', label = 'Linearizacija')
plt.title('s - t^2 graf')
plt.xlabel('t^2')
plt.ylabel('s')
plt.legend()
plt.grid(True)
plt.show()

# (c) Koristeći se prethodnim koracima izračunajte moment tromosti Iz 
# i njegovu pripadnu izvedenu pogrešku

#a_ef = mgr^2/mr^2 + I_z
#I_z = mr^2 (g/a_ef -1)

mr2 = m * r**2

#za log(s) - log(t)
Iz_a = mr2 * ((g/a_ef_a) - 1)
#derivacija dIz/da_f = mgr^2 * (-1 * a_ef^-2) = -mgr^2/a_ef^2
devi_Iz_a  = ((mr2*g)/a_ef_a**2) * devi_a_ef_a


#za s - t^2
Iz_b = mr2 * ((g/a_ef_b) - 1)
devi_Iz_b  = ((mr2*g)/a_ef_b**2) * devi_a_ef_b

print('-'*50)
print('Tromost Iz i pripadne pogreske')
print('-'*50)
print('log(s) - log(t) graf')
print(f'Iz = ({Iz_a:.4e} +- {devi_Iz_a:.4e}) kg m^2')
print(f'(a_ef = {a_ef_a:.4f} +- {devi_a_ef_a:.4f} m/s^2)')
print('-'*50)
print('s - t^2 graf')
print(f'Iz = ({Iz_b:.4e} +- {devi_Iz_b:.4e}) kg m^2')
print(f'(a_ef = {a_ef_b:.4f} +- {devi_a_ef_b:.4f} m/s^2)')