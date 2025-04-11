import numpy as np
import matplotlib.pyplot as plt


v0 = int(input("Unesite iznos početne brzine: "))  
theta = int(input("Unesite kut otklona: ")) 

theta_rad = np.radians(theta)

g = 9.81

t_max = 10 
dt = 1 
t = np.arange(0, t_max+1, dt) 

v0x = v0 * np.cos(theta_rad)  
v0y = v0 * np.sin(theta_rad)

x = 0
y = 0
vx=v0x
vy=v0y

x_vri=[]
y_vri=[]
vx_vri=[]
vy_vri=[]

for i in t:
    x = v0x * i
    y = v0y * i - 0.5 * g * i**2
    vy=v0y-g*i
    x_vri.append(x)
    y_vri.append(y)
    vx_vri.append(v0x)
    vy_vri.append(vy)



plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x_vri, y_vri, label='x-y',color='green')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Putanja cestice (x - y)')



plt.subplot(3, 1, 2)
plt.plot(t, x_vri, label='x-t', color='cyan')
plt.xlabel('Vrijeme [s]')
plt.ylabel('X [m]')


plt.subplot(3, 1, 3)
plt.plot(t, y_vri, label='y-t', color='blue')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Y [m]')


plt.tight_layout()
plt.show()