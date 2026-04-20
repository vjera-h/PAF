import numpy as np

def differentiate_point(func, x, h=0.01, method='three-step'):
    """Numerička derivacija u točki."""
    if method == 'two-step':
        return (func(x + h) - func(x)) / h
    else:  # three-step (centralna diferencija)
        return (func(x + h) - func(x - h)) / (2 * h)

def differentiate_range(func, a, b, h=0.01, method='three-step'):
    """Numerička derivacija na rasponu."""
    x_values = np.arange(a, b, h)
    y_derivatives = [differentiate_point(func, x, h, method) for x in x_values]
    return x_values, y_derivatives


def integrate_rectangles(func, a, b, n):
    """Pravokutna aproksimacija (vraća donju i gornju među)."""
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    
    # Donja i gornja suma (ovisno o monotonosti na podintervalu)
    # Pojednostavljeno koristimo lijevu i desnu sumu kao aproksimacije međa
    f_vals = func(x)
    lower_sum = np.sum(np.minimum(f_vals[:-1], f_vals[1:])) * dx
    upper_sum = np.sum(np.maximum(f_vals[:-1], f_vals[1:])) * dx
    
    return lower_sum, upper_sum

def integrate_trapezoid(func, a, b, n):
    """Integracija trapeznom formulom."""
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    return (dx / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])