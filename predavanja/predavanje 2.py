#predavanje 2
#eksplicitna metoda - Euler
#dP/dt -> (P_{i+1} - P_{i})/delta t

import matplotlib.pyplot as plt
import numpy as np

P0 = 10000
r = 0.9
T = 10 #godina

dt = 1 #godina

t = np.arange(0, T, dt)
#P = [P0] ovako ili:
P = np.zeros(len(t))
P[0] = P0
for i in range(0, len(t)):
    P[i+1] = P[i] + P[i]*r*dt #ovdje nesto ne valjaaaaaaa

plt.figure()
plt.plot(t,P)
plt.show()