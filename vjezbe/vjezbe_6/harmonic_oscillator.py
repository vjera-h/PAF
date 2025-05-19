import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0, dt):
        self.m = m            # masa
        self.k = k            # konstanta opruge
        self.x = x0           # pocetni polozaj
        self.v = v0           # pocetna brzina
        self.a = -k * x0 / m  # pocetna akceleracija
        self.dt = dt          # vremenski korak

        self.x_values = [x0]
        self.v_values = [v0]
        self.a_values = [self.a]
        self.t_values = [0]

    def korak(self):

        self.a = -self.k * self.x / self.m
        self.v += self.a * self.dt
        self.x += self.v * self.dt

    def sim(self, t_max):
        t = 0
        while t < t_max:
            self.korak()
            t += self.dt
            self.x_values.append(self.x)
            self.v_values.append(self.v)
            self.a_values.append(self.a)
            self.t_values.append(t)

    def graf(self):
        plt.figure(figsize=(10, 6))
        plt.subplot(3,1,1)
        plt.plot(self.t_values, self.x_values, label='x(t) - položaj')
        plt.xlabel(' t/s')
        plt.ylabel('x(t)/m')
    
        plt.subplot(3,1,2)
        plt.plot(self.t_values, self.v_values, label=('v(t) - brzina'))
        plt.xlabel('t/s')
        plt.ylabel('v(t)/m/s')
        
        plt.subplot(3,1,3)
        plt.plot(self.t_values, self.a_values, label='a(t) - ubrzanje')
        plt.xlabel('t/s')
        plt.ylabel('a(t)/m/s^2')
        plt.show()
        
    def izracunaj_period(self):
        x0 = self.x_values[0]
        prijelazi = []

        for i in range(1, len(self.x_values)):
            if self.x_values[i-1] < x0 and self.x_values[i] >= x0:
                if self.v_values[i] > 0:
                    prijelazi.append(self.t_values[i])

        if len(prijelazi) >= 2:
            period = prijelazi[1] - prijelazi[0]
            return period
        
        return None