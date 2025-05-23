import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, k, m, R, dt):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(k))
        self.vy = v0 * np.sin(np.radians(k))
        self.m = m
        self.k = R
        self.dt = dt
        self.g = 9.81

        
        self.putanja_x = [self.x]
        self.putanja_y = [self.y]


      

    def koraci(self):
        ax = -self.k/self.m * self.vx
        ay = -self.g - self.k/self.m * self.vy

        
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        self.putanja_x.append(self.x)
        self.putanja_y.append(self.y)

    def euler_simulacija(self):
        while self.y >= 0:
            self.koraci()
        return self.putanja_x, self.putanja_y
    

    def acc(self, vx, vy):
        ax = -self.k/self.m * vx
        ay = -self.g - self.k/self.m * vy
        return ax, ay
    
    def rk4_simulacija(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]
        dt = self.dt

        while y >= 0:
            
            ax1, ay1 = self.acc(vx, vy)
            k1vx, k1vy = ax1*dt, ay1*dt
            k1x, k1y = vx*dt, vy*dt

            
            ax2, ay2 = self.acc(vx + k1vx/2, vy + k1vy/2)
            k2vx, k2vy = ax2*dt, ay2*dt
            k2x, k2y = (vx + k1vx/2)*dt, (vy + k1vy/2)*dt

            
            ax3, ay3 = self.acc(vx + k2vx/2, vy + k2vy/2)
            k3vx, k3vy = ax3*dt, ay3*dt
            k3x, k3y = (vx + k2vx/2)*dt, (vy + k2vy/2)*dt

            
            ax4, ay4 = self.acc(vx + k3vx, vy + k3vy)
            k4vx, k4vy = ax4*dt, ay4*dt
            k4x, k4y = (vx + k3vx)*dt, (vy + k3vy)*dt

        
            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
            x += (k1x + 2*k2x + 2*k3x + k4x)/6
            y += (k1y + 2*k2y + 2*k3y + k4y)/6

            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y