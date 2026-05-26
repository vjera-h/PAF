#Napišite modul "calculus.py" koji će sadržavati dvije metode:

import numpy as np
import matplotlib.pyplot as plt

def derivacija_tocka(f, x, epsilon = 1e-5, metoda = 'three step'):
    """Prva metoda kao ulazne parametre prima funkciju i točku, 
    a kao rezultat vraća vrijednost derivacije funkcije u toj točki."""
    if metoda == 'two step': #unaprijedna diferencija
            return (f(x + epsilon) - f(x))/epsilon
    elif metoda == 'three step': #cenralna diferencija
            return (f(x + epsilon) - f(x - epsilon))/(2 * epsilon)
    else:
        raise ValueError ('Metoda nije prepoznata, upišite "two step" ili "three step".')
        
def derivacija_raspon(f, x_min, x_max, epsilon = 1e-5, metoda = 'three step', ):
    """Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije. 
    Funkcija korisniku vraća listu točaka u kojima će biti izvršena numerička derivacija 
    zadanom rasponu i iznose derivacije funkcije u tim istim točkama."""
    korak = np.linspace(x_min, x_max, 500)
    derivacije = []
    for x in korak:
        deriv = derivacija_tocka(f, x, epsilon, metoda)
        derivacije.append(deriv)
    return korak, derivacije

#U modulu "calculus.py" implementirajte nove dvije metode:

def pravokutna_aproksimacija(f, a, b, podjela):
    """Prva metoda kao ulazne parametre prima funkciju, granice integracije(interval [a, b]) i 
    broj podjela za numeričku integraciju(broj pravokutnika na koje se dijeli interval),
    a vraća gornju i donju među koristeći pravokutnu aproksimaciju."""
    dx = (b - a) / podjela #sirina svakog pojedinacnog podintervala
    suma_lijeva = 0
    suma_desna = 0

    for p in range(0, podjela): #petlja za svaki od pravokutnika
        #lijeva
        xi_l = a + p * dx #tocka podjele intervala, ako je pocetak intervala a, onda se treba zbrojit da se ne bi racunalo od 0
        suma_lijeva += f(xi_l) * dx
        #desna
        xi_d = a + (p + 1) * dx
        suma_desna += f(xi_d) * dx
    return suma_lijeva, suma_desna
     
def trapezna_aproksimacija(f, a, b, podjela):
    """Druga metoda ima iste ulazne parametre a vraća numeričku vrijednost 
    integrala koristeći trapeznu formulu."""
    #formula: dx/2 * (f(x0) + 2*f(x1) + ... + 2*f(xn-1) + f(xn))
    dx = (b - a) / podjela 
    suma = (f(a) + f(b))/2
    for p in range(1, podjela): #od 1 do do podjela - 1, tj. p prolazi kroz sve unutarnje točke
        tocke = a + p * dx
        suma += f(tocke) #za svaki p u podjeli 
    return suma * dx