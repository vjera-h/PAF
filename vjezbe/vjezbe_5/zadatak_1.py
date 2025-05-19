import numpy as np
import matplotlib.pyplot as plt
import calculus as cals


def kubna(x):
    return x**3


def sinus(x):
    return np.sin(x)


x_k, deriv_k = cals.deriv_u_rasponu(kubna, -2, 2)

x_s,deriv_sin = cals.deriv_u_rasponu(sinus, 0, 2 * np.pi)

    
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_k, deriv_k, label = 'numericka derivacija')
plt.title('derivacija kubne funkcije')
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(x_s,deriv_sin, label = 'numericka derivacija')
plt.title('derivacija sinus')
plt.legend()

plt.tight_layout()
plt.show()