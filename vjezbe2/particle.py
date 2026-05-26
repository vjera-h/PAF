#U zasebnom modulu "particle.py" definirajte klasu Particle za čestice koja će imati 
#atribute početne brzine, kuta otklona i koordinata početnog položaja. 
#Neka klasa sadrži i sljedeće metode:
#• metodu reset() koja briše sve informacije o čestici
#• privatnu metodu __move() koja pomiče česticu za korak ∆t
#• metodu range() koja numerički računa domet projektila
#• metodu plot_trajectory() koja crta putanju u x − y ravnini za trenutno stanje čestice.


import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0, y0): 
        """Initializacija koda, sadrži atribute početne brzine, kuta otklona i koordinate početnog položaja"""
    #__init__ je initialization, self je prvi argument u metodi- novi objekt
        self.v0 = v0 #m/s
        #v0 je vrijednost u Particle projektu, self.v0 je polje koje pohranjuje vrijednost
        self.theta = np.radians(theta) #pretvara iznos theta u radijane
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81 #m/s^2

        self.x = [self.x0] 
        self.y = [self.y0]
        #brzine vx = v0 * cos(theta), vy = v0 * sin(theta)
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = [0] #vrijeme
        self.reset()

    def reset(self):
        """Briše sve informacije o čestici"""
        #u stvarnosti ne briše atribute, tada bi se objekt razbio
        self.x = [self.x0] 
        self.y = [self.y0]
        #brzine vx = v0 * cos(theta), vy = v0 * sin(theta)
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = [0] #vrijeme

    def  __move(self, dt):
        """Pomiče česticu za korak ∆t"""
        #pomak koordinata x = x0 + vx * dt, y = y0 + vy * dt
        self.x.append(self.x[-1] + self.vx * dt) #[-1] zadnji element zadnja poznata velicina
        self.y.append(self.y[-1] + self.vy * dt)
        #vy = vy - g * dt
        self.vy = self.vy - self.g * dt
        #vx = konst.
    
    def range(self, dt):
        """Numerički računa domet projektila"""
        self.reset() #da resetira sve atribute
        while self.y[-1]>=0 or self.vy>0: #mjeri pomak prije nego što projektil dođe do poda
            self.__move(dt)
        #domet je zadnje izmjerena x koordinata, tj. kada je y=0 x=domet
        return self.x[-1]

    def plot_trajectory(self, dt):
        self.reset()
        while self.y[-1]>=0:
            self.__move(dt)
        plt.plot(self.x, self.y, color = 'blue')
        plt.title('Graf putanje')
        plt.xlabel('x')
        plt.ylabel('y')  
        plt.axhline(0, color = 'black', lw = 0.5)
        plt.axvline(0, color = 'black', lw = 0.5)
        plt.grid()
        plt.show()
