import numpy as np
import matplotlib.pyplot as plt
from particle import Particle

# Parametri
v0 = 10
theta = 60
g = 9.81

# Analitički domet: R = (v0^2 * sin(2*theta)) / g
analytical_range = (v0**2 * np.sin(2 * np.radians(theta))) / g

p = Particle(v0, theta, 0, 0)
num_range = p.range(0.001)

print(f"Analitički domet: {analytical_range:.4f} m")
print(f"Numerički domet (dt=0.001): {num_range:.4f} m")
print(f"Odstupanje: {abs(analytical_range - num_range):.4f} m")

# Zadatak 2: Relativna pogreška u ovisnosti o dt
dt_values = np.linspace(0.001, 0.1, 100)
errors = []

for dt in dt_values:
    num_r = p.range(dt)
    relative_error = abs(num_r - analytical_range) / analytical_range * 100
    errors.append(relative_error)

plt.figure(figsize=(8, 5))
plt.plot(dt_values, errors)
plt.xlabel('Vremenski korak dt [s]')
plt.ylabel('Relativna pogreška [%]')
plt.title('Relativna pogreška numeričkog rješenja ovisno o dt')
plt.grid(True)
plt.show()