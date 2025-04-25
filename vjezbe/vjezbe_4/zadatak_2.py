import numpy as np
import matplotlib.pyplot as plt
from zadatak_1 import particle 

v0 = 10
theta = 60
g = 9.81

d_exact = (v0**2 * np.sin(2 * np.radians(theta))) / g

dt_values = np.logspace(-1, -4, 20)

errors = []
for dt in dt_values:
    p = particle(v0, theta)
    d_numeric = p.range(dt)
    error = abs(d_numeric - d_exact) / d_exact
    errors.append(error)

plt.figure(figsize=(10, 6))
plt.loglog(dt_values, errors, 'o-', label='Relativna pogreška')
plt.xlabel('Vremenski korak Δt (s)')
plt.ylabel('Relativna pogreška')
plt.title('Ovisnost pogreške o Δt (v0=10 m/s, θ=60°)')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.show()