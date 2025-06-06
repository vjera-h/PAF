import numpy as np
import matplotlib.pyplot as plt


G = 6.67408e-11 
MS = 1.989e30  
MZ = 5.9742e24   


r_s = np.array([0.0, 0.0])
v_s = np.array([0.0, 0.0])
r_z = np.array([1.486e11, 0.0])
v_z = np.array([0.0, 29783.0])

dt = 60 * 60
k = int(365.242 * 24)

x_s = []
y_s = []
x_z = []
y_z = []

for i in range(k):
    r = r_z - r_s
    udalj = (r[0]**2 + r[1]**2)**0.5  
    
    F = G * MS * MZ / udalj**2
    F_vek = F * r / udalj
    
    a_s = F_vek / MS
    v_s = v_s + a_s * dt
    r_s = r_s + v_s * dt
    a_z = -F_vek / MZ
    v_z = v_z + a_z * dt
    r_z = r_z + v_z* dt

    x_s.append(r_s[0])
    y_s.append(r_s[1])
    x_z.append(r_z[0])
    y_z.append(r_z[1])

plt.plot(x_s, y_s, label='Sunce')
plt.plot(x_z, y_z, label='Zemlja')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Sunca i Zemlje')
plt.axis('equal')
plt.legend()
plt.show()