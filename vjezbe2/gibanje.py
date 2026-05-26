#Koristeći klasu Particle u programu "gibanje.py" kreirajte jednan objekt i 
#postavite ga na neke od vrijednosti za koje ste analitički izračunali domet. 
#Da li se numeričko riješenje slaže s analitičkim? Koliko je odstupanje?

import numpy as np
from particle import Particle

x0 = 0 #m
y0 = 0 #m
dt = 0.001

g = 9.81 #m/s^2
v0 = 15 #brzina m/s
theta = 55 #kut u stupnjevima
theta_r = np.radians(theta) #kut u radijanima

objekt_numericko = Particle(v0, theta, x0, y0)
R_num = objekt_numericko.range(dt)

R = v0**2 * np.sin(2 * theta_r) / g #R = v0 * sin(2theta)/g

odstupanje = R_num - R

print(f'Analitički domet je {R} m \nNumerički domet je {R_num}\nOdstupanje je {odstupanje}')

#Numeričko i analitičko rješenje se večinom slažu.

