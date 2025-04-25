import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self, v0, theta, x0=0, y0=0):
        self.v0 = v0
        self.theta = np.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.trajectory_x = [self.x]
        self.trajectory_y = [self.y]

    def __move(self, dt):
        g = 9.81 
        self.x += self.vx * dt
        self.vy -= g * dt 
        self.y += self.vy * dt
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x - self.x0
    def plot_trajectory(self, dt=0.01):
        self.reset()
        
        while self.y >= 0:
            self.__move(dt)
        
        plt.figure(figsize=(8, 4))
        plt.plot(self.trajectory_x, self.trajectory_y, label='Putanja čestice')
        plt.scatter([self.x0], [self.y0], color='red', label='Početak')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Putanja projektila')
        plt.grid()
        plt.legend()
        plt.show()