#Za česticu početne brzine v0 = 10 m/s i kuta otklona θ = 60o nacrtajte graf ovisnosti 
#relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka ∆t.

import numpy as np
import matplotlib.pyplot as plt
from particle import Particle

#zadane vrijednosti
v0 = 10 #m/s
theta = 60 #kut u stupnjevima
theta_r = np.radians(theta) #kut u radijanima
x0 = 0
y0 = 0
g = 9.81 #m/s^2

#analitičko rješenje
R_ana = (v0**2 * np.sin(2 * theta_r)) / g #R = v0 * sin(2theta)/g

dt_korak = np.linspace(0.001,0.1, 1000) #počinje sa 0.001, završava sa 0.1, 10 vrijednosti

#numeričko rješenje i relativna pogreška
relativna = []

for dt in dt_korak:
    objekt_numericko = Particle(v0, theta, x0, y0) #inicijalizacija cestice
    R_num = objekt_numericko.range(dt)
    pogreska = (abs(R_num - R_ana)/abs(R_ana)) * 100
    relativna.append(pogreska)

plt.figure()
plt.plot(dt_korak, relativna, color = 'blue')
plt.title('Graf ovisnosti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka ∆t', fontsize = 9)
plt.xlabel('∆t')
plt.ylabel('Relativna pogreska [%]')  
plt.axhline(0, color = 'black', lw = 0.5)
plt.axvline(0, color = 'black', lw = 0.5)
plt.grid(True)
plt.show()