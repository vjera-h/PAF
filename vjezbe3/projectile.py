# Napišite kod koji sadrži klasu Projectile koja ima implementirane metode za 
# simuliranje kosog hitca u dvije dimenzije s otporom zraka. 
# Testirajte za koji korak ∆t Euler-ova metoda daje dovoljno precizno numeričko
# rješenje koje na x − y grafu nema naznake ne-fizikalnog gibanja.

import numpy as np
import matplotlib.pyplot as plt


class Projectile:
    def __init__(self, x0, y0, v0, theta, m, A, C = 0.35):
        """Initializacija koda, sadrži atribute početne brzine, kuta otklona i koordinate početnog položaja"""
        self.v0 = v0 #m/s pocetna brzina
        #v0 je vrijednost u Particle projektu, self.v0 je polje koje pohranjuje vrijednost
        self.theta = np.radians(theta) #pretvara iznos theta u radijane
        self.x0 = x0
        self.y0 = y0
        self.m = m #kg
        self.A = A #povrsina poprecnog presjeka
        self.C = C #koeficijent aerodinamicnog otpora C = 0.35 za prosjecne obiteljske automobile

        self.g = 9.81 #m/s^2
        self.rho = 1.225 #kg/m^3 gustoca zraka

        #sila otpora zraka F = 1/2 * C * A * rho * v**2
        self.k = (self.C * self.A * self.rho)/2 #konstanta 

        self.xE = [self.x0]
        self.yE = [self.y0]

        self.xR = [self.x0] 
        self.yR = [self.y0]
        #brzine vx = v0 * cos(theta), vy = v0 * sin(theta)
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = [0] #vrijeme
        self.reset()

    def reset(self):
        """Briše sve informacije o čestici"""
        #u stvarnosti ne briše atribute, tada bi se objekt razbio
        self.xE = [self.x0]
        self.yE = [self.y0]

        self.xR = [self.x0] 
        self.yR = [self.y0]
        #brzine vx = v0 * cos(theta), vy = v0 * sin(theta)
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = [0] #vrijeme

    def  __move_Euler(self, dt):
        """Pomiče česticu za korak ∆t"""
        # Ukupna brzina v
        v = np.sqrt(self.vx**2 + self.vy**2)

        # d**2x / dt**2 = - (k * vx * v)/m = ax
        ax = - (self.k * v * self.vx) / self.m
        # d**2y / dt**2 = - g - (k * vy * v)/m = ay
        ay = - self.g - (self.k * v * self.vy) / self.m

        #vy = vy - ay * dt ali koristimo + jer su akceleracije vec negativne
        self.vy += ay * dt
        #vx = vx - ax * dt
        self.vx += ax * dt

        #pomak koordinata x = x0 + vx * dt, y = y0 + vy * dt
        #Eulerova metoda
        self.xE.append(self.xE[-1] + self.vx * dt) #[-1] zadnji element
        self.yE.append(self.yE[-1] + self.vy * dt) #zadnja poznata velicina je x0

        self.t.append(self.t[-1] + dt)

    #Klasi Projectile dodajte mogućnost rješavanja problema uz pomoć Runge-Kutta metode 4. reda.
    
    def __derivacije(self, vx, vy):
        """Pomoćna funkcija koja vraća derivacije (vx, vy, ax, ay)"""
        v = np.sqrt(vx**2 + vy**2)
        ax = - (self.k * v * vx) / self.m
        ay = - self.g - (self.k * v * vy) / self.m
        return vx, vy, ax, ay
    
    def __move_rk4(self, dt):
        """Pomiče česticu koristeći Runge-Kutta metodu 4. reda"""
        #trenutna stanja
        tren_x, tren_y = self.xR[-1], self.yR[-1]
        tren_vx, tren_vy = self.vx, self.vy

        #k1 - početak intervala
        k1_dx, k1_dy, k1_dvx, k1_dvy = self.__derivacije(tren_vx, tren_vy)

        #k2 - sredina intervala koristeći k1
        k2_dx, k2_dy, k2_dvx, k2_dvy = self.__derivacije(tren_vx + k1_dvx * dt/2, tren_vy + k1_dvy * dt/2)

        #k3 - sredina intervala koristeći k2
        k3_dx, k3_dy, k3_dvx, k3_dvy = self.__derivacije(tren_vx + k2_dvx * dt/2, tren_vy + k2_dvy * dt/2)

        #k4 - kraj intervala koristeći k3
        k4_dx, k4_dy, k4_dvx, k4_dvy = self.__derivacije(tren_vx + k3_dvx * dt, tren_vy + k3_dvy * dt)

        #Ažuriranje pozicija (x, y) koristeći ponderirani prosjek nagiba brzina
        novo_x = tren_x + (dt / 6.0) * (k1_dx + 2*k2_dx + 2*k3_dx + k4_dx)
        novo_y = tren_y + (dt / 6.0) * (k1_dy + 2*k2_dy + 2*k3_dy + k4_dy)

        # Ažuriranje brzina (vx, vy) koristeći ponderirani prosjek akceleracija
        self.vx = tren_vx + (dt / 6.0) * (k1_dvx + 2*k2_dvx + 2*k3_dvx + k4_dvx)
        self.vy = tren_vy + (dt / 6.0) * (k1_dvy + 2*k2_dvy + 2*k3_dvy + k4_dvy)

        self.xR.append(novo_x)
        self.yR.append(novo_y)
        self.t.append(self.t[-1] + dt)

    def plot_trajectory(self, dt):
        self.reset()
        while self.yE[-1]>=0:
            self.__move_Euler(dt)
        #podatci se spremaju u liste kako bi se ocuvali nakon resetiranja
        xe_plot, ye_plot = list(self.xE), list(self.yE)

        self.reset()
        while self.yR[-1]>=0:
            self.__move_rk4(dt)

        plt.plot(xe_plot, ye_plot, color = 'blue', label = 'Euler metoda')
        plt.plot(self.xR, self.yR, color = 'pink', label = 'Runge-Kutta metoda 4. reda')
        plt.title('Graf putanje')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')  
        plt.axhline(0, color = 'black', lw = 0.5)
        plt.axvline(0, color = 'black', lw = 0.5)
        plt.grid()
        plt.show()

# Usporedite putanje projektila preko Euler-ove i Runge-Kutta metode za ∆t = 0.01.

metode = Projectile(0, 0, 10, 45, 1, A = 0.1)
metode.plot_trajectory(0.01)