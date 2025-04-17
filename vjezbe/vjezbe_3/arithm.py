import numpy as np
import math as m
import matplotlib.pyplot as plt
x = [12.5, 3.2, 48.6, 25.1, 24, 67, 12.7, 55.2, 7.6, 10]
suma_x = 0
for i in x :
    suma_x += 1
avg_x = suma_x/len(x)

sigma_x = 0
for i in x:
    sigma_x += (i - avg_x)**2
sigma_x = m.sqrt(sigma_x/len(x))

plt.figure()
plt.plot(x,marker = 'o',markersize = 5, c = 'cyan', label = 'podatci')
plt.axhline(avg_x, c = 'b', label = 'avg_x')
plt.axhline(avg_x + sigma_x, c = 'black',label = 'sigma_x')
plt.axhline(avg_x - sigma_x, c = 'red')

plt.show()