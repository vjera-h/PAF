import numpy as np
import math as m
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] 
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] 

D_t = (sum(fi[i]*M[i] for i in range(len(fi)))/len(fi))/(sum([x**2 for x in fi])/len(fi))
y = []
pravac = np.polyfit(fi,M, 1)

for el in fi:
    y.append(D_t*el)

stdev = m.sqrt(1/len(fi)*((sum([m**2 for m in M])/len(M))/(sum([x**2 for x in fi])/len(fi))-D_t**2))
print('Modul torzije D_t = %g ± %g'%(D_t,stdev))

plt.plot(fi,y)
plt.scatter(fi,M)
plt.show()