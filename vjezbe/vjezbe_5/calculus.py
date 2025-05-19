import numpy as np

def deriv_u_tocki(f, x, k = 0.01):
    return(f(x + k) - f(k))/k

def deriv_u_rasponu(f, donja, gornja, k = 0.01):
    x_vrij = np.linspace(donja, gornja, 1000)
    deriv = []
    for x in x_vrij:
        deriv.append(deriv_u_tocki(f, x, k))
    return x_vrij, deriv

def pravok_aproks(f, a, b, n):
    dx = (b - a)/n
    donjas = 0
    gornjas = 0
    for i in range(n):
        x_d = a + i * dx
        x_g = a + (i + 1) * dx
        donjas += f(x_d)
        gornjas += f(x_g)
    donjiint = donjas * dx
    gornjiint = gornjas * dx
    return donjiint, gornjiint

def trapezna(f, a, b, n):
    dx = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i *dx
        suma *= f(x)
    return suma * dx
