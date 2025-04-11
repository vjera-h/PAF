import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(brzina,vrijeme, dt=1):
    t = np.arange(0, vrijeme, dt)
    v=np.full_like(t,brzina)
    x=brzina*t


    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, x, label="Polozaj (x)", color="purple")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Polozaj [m]")
    
    
    plt.subplot(2, 1, 2)
    plt.plot(t, v, label="Brzina (v)", color="pink")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    
    plt.tight_layout()
    plt.show()




def kosi_hitac(v0, theta, masa, vrijeme, dt=0.1):
    theta_rad = np.radians(theta)
    
    v_x0 = v0 * np.cos(theta_rad)
    v_y0 = v0 * np.sin(theta_rad)
    g = 9.81
    
    t = np.arange(0, vrijeme + dt, dt)
    x_vrijednosti=[]
    y_vrijednosti = []
    
    for i in t:
        x = v_x0 * i
        y = v_y0 * i - 0.5 * g * i**2
        x_vrijednosti.append(x)
        y_vrijednosti.append(y)
    



    

    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(x_vrijednosti , y_vrijednosti, label="Putanja")
    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")
    

    plt.subplot(3, 1, 2)
    plt.plot(t, x_vrijednosti, label="x(t)", color="blue")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("X [m]")
    

    plt.subplot(3, 1, 3)
    plt.plot(t, y_vrijednosti, label="y(t)", color="red")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Y [m]")

    plt.tight_layout()
    plt.show()