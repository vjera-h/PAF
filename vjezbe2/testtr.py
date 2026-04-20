import calculus
import matplotlib.pyplot as plt
import numpy as np

# Primjer funkcije: sin(x)
f = lambda x: np.sin(x)
f_prime_analiticki = lambda x: np.cos(x)
f_int_analiticki = 2.0 # Integral sin(x) od 0 do pi

# Graf derivacije
x_an = np.linspace(0, 2*np.pi, 100)
plt.plot(x_an, f_prime_analiticki(x_an), 'k', label='Analitički', lw=2)

for h in [0.1, 0.5]:
    x_num, y_num = calculus.differentiate_range(f, 0, 2*np.pi, h=h, method='three-step')
    plt.scatter(x_num, y_num, label=f'Numerički h={h}')

plt.legend()
plt.title("Usporedba derivacija")
plt.show()

# Graf integracije (ovisnost o broju koraka N)
n_values = range(2, 50)
trap_errors = []
for n in n_values:
    res = calculus.integrate_trapezoid(f, 0, np.pi, n)
    trap_errors.append(abs(res - f_int_analiticki))

plt.plot(n_values, trap_errors)
plt.yscale('log')
plt.xlabel('Broj podjela n')
plt.ylabel('Apsolutna pogreška integrala')
plt.title('Konvergencija trapezne metode')
plt.grid(True)
plt.show()