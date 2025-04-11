import numpy as np
import matplotlib.pyplot as plt

F = int(input("Upisite iznos sile: "))  
m = int(input("Upisite masu čestice: ")) 

t_max = 10 
dt = 1
t = np.arange(0, t_max+1, dt) 

x0 = 0 
v0 = 0  
a = F / m 

brz=[]
pomaci=[]
akc=[]


x = x0
v = v0

for i in t:
    if i == 0:
        brz.append(v0)
        pomaci.append(x0)
        akc.append(a)
    else:
        v = v + a * dt 
        x = x + v * dt + 0.5 * a * dt**2  
        brz.append(v)
        pomaci.append(x)
        akc.append(a)



plt.figure(figsize=(12, 8))


plt.subplot(3, 1, 1)
plt.plot(t, pomaci, label='Položaj (x)', color='red')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Položaj (x) [m]')


plt.subplot(3, 1, 2)
plt.plot(t, brz, label='Brzina (v)', color='black')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Brzina (v) [m/s]')

plt.subplot(3, 1, 3)
plt.plot(t, akc, label='Akceleracija (a)', color='blue')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Akceleracija (a) [m/s^2]')


plt.tight_layout()
plt.show()