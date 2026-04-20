import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = np.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.reset()
        self.g = 9.81

    def reset(self):
        """Resetira česticu na početne vrijednosti."""
        self.x = [self.x0]
        self.y = [self.y0]
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = [0]

    def __move(self, dt):
        """Privatna metoda koja pomiče česticu za korak dt."""
        self.x.append(self.x[-1] + self.vx * dt)
        self.vy -= self.g * dt
        self.y.append(self.y[-1] + self.vy * dt)
        self.t.append(self.t[-1] + dt)

    def range(self, dt=0.01):
        """Numerički računa domet projektila."""
        self.reset()
        while self.y[-1] >= 0:
            self.__move(dt)
        return self.x[-1]

    def plot_trajectory(self, dt=0.01):
        """Crta putanju čestice."""
        self.range(dt)
        plt.plot(self.x, self.y)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('Putanja projektila')
        plt.grid(True)
        plt.show()