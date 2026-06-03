#Napišite funkciju volumen_valjka(R, L) koja prima R i L u centimetrima 
# i vraća volumen u cm3 i funkciju sigma_volumena(R, sigma_R, L, sigma_L) 
# koja računa standardnu devijaciju volumena po formuli za propagaciju pogreške. 
# Izračunajte i ispišite rezultate u znanstvenom zapisu za sva tri valjka.

import numpy as np


def volumen_valjka(R, L):
    #V = R**2  * pi * L
    V = []
    for r,l in zip(R,L):
        v = r**2 * np.pi * l
        V.append(v)
    return V

def sigma_volumena(R, sigma_R, L, sigma_L):
    #propagacija sigma_V = sqrt((dV/dR * sigma_R)^2 + (dV/dL * sigma_L)^2)
    #V = R^2 * pi * L
    #derivacije dV/dR = 2RpiL dV/dL = R^2pi
    sigma_V = []
    for r,l in zip(R,L):
        dR = 2 * r * np.pi * l
        dL = r**2 * np.pi
        sigma = np.sqrt((dR * sigma_R)**2 + (dL * sigma_L)**2)
        sigma_V.append(sigma)
    return sigma_V

#Napravite izračune kao i u prethodnom zadatku, ali za gustoće valjaka.

def gustoca_valjka(m, V):
    #rho = m/V
    rho = []
    for M,v in zip(m,V):
        rh = M/v
        rho.append(rh)
    return rho

def sigma_gustoca(V, sigma_V, m, sigma_m):
    #propagacija sigma_rho = sqrt((drho/dV * sigma_V)^2 + (drho/dm * sigma_m)^2)
    #rho = m/V
    #derivacije drho/dV = -m/V^2 drho/dm = 1/V
    sigma_rho = []
    for M,v,sig_v in zip(m,V,sigma_V):
        dV = -M/v**2
        dm = 1/v
        sigma = np.sqrt((dV * sig_v)**2 + (dm * sigma_m)**2)
        sigma_rho.append(sigma)
    return sigma_rho

def aritmeticka_sredina(brojevi):
    n = len(brojevi)
    sredina = sum(brojevi) / n
    return sredina

def standardna_devijacija(brojevi):
    n = len(brojevi)
    suma = sum((b - aritmeticka_sredina(brojevi))**2 for b in brojevi)
    nazivnik = n * (n - 1)
    devijacija = np.sqrt(suma/nazivnik)
    return devijacija

R_lista = [np.array([9.99, 10.09, 10.05, 10.04, 9.87]), 
     np.array([9.96, 9.91, 9.98, 9.99, 9.94]),
     np.array([12.48, 12.49, 12.49, 12.46, 12.47])] #mm

L_lista = [np.array([49.8, 49.0, 50.48, 49.8, 49.96]),
     np.array([52.56, 52.5, 52.62, 52.58, 52.54]),
     np.array([55.34, 55.4, 55.3, 55.44, 55.48])] #mm

m_lista = [np.array([138.98, 139.98, 139.2, 138.9, 138.92]),
     np.array([128.65, 128.6, 128.65, 128.35, 128.5]),
     np.array([71.89, 71.9, 71.79, 71.85, 71.7])] #g

rho_sredina_lista = []

print('ZADATCI 2 i 3')

for i in range(3):
    R = [r * 0.1 for r in R_lista[i]] #iz mm u cm
    L = [l * 0.1 for l in L_lista[i]]
    m = m_lista[i] #g

    #sredine i sigme za ulazne parametre
    R_sredina = aritmeticka_sredina(R)
    sigma_R = standardna_devijacija(R)

    L_sredina = aritmeticka_sredina(L)
    sigma_L = standardna_devijacija(L)

    m_sredina = aritmeticka_sredina(m)
    sigma_m = standardna_devijacija(m) #ispada konstanta tkd u funkciji sigma_gustoca ga ne odvajam u for petlji

    #funkcije
    V_lista_rez = volumen_valjka(R, L)
    V_sredina = aritmeticka_sredina(V_lista_rez)
    
    sigma_V_lista_rez = sigma_volumena(R, sigma_R, L, sigma_L)
    sigma_V_sred = aritmeticka_sredina(sigma_V_lista_rez)
    
    rho_lista_rez = gustoca_valjka(m, V_lista_rez)
    rho_sredina = aritmeticka_sredina(rho_lista_rez)
    rho_sredina_lista.append(rho_sredina)
    
    sigma_rho_lista_rez = sigma_gustoca(V_lista_rez, sigma_V_lista_rez, m, sigma_m)
    sigma_rho_sred = aritmeticka_sredina(sigma_rho_lista_rez)

    print('-'*50)
    print(f'Valjak {[i+1]}')
    #:.3e određuje broj decimala i stavlja u znanstveni zapis
    print(f'R = ({R_sredina:.3e} +- {sigma_R:.3e}) cm') 
    print(f'L = ({L_sredina:.3e} +- {sigma_L:.3e}) cm')
    print(f'm = ({m_sredina:.3e} +- {sigma_m:.3e}) g')
    print(' '*50)
    print(f'V = ({V_sredina:.3e} +- {sigma_V_sred:.3e}) cm^3')
    print(f'rho = ({rho_sredina:.3e} +- {sigma_rho_sred:.3e}) g/cm^3')

#Na temelju izračunatih gustoća odredite od kojeg je materijala svaki valjak 
# te izračunajte relativnu pogrešku

#literaturne gustoce g/cm^3
rho_lit_lista = [['aluminij', 2.70], ['zeljezo', 7.87], ['mesing', 8.73]]
#rho_sredina_za_lit je lista rezultata

print('-' * 50)
print('ZADATAK 4')  

rho_sredina_za_lit = [['valjak 1'], ['valjak 2'], ['valjak 3']]


def pogreska_gustoca(rho, rho_lit):
    #sigma_rho = abs(rho - rho_lit)/rho_lit * 100 %
    sigma_rho = []
    for r in rho:
        sigma = abs(r - rho_lit)/rho_lit * 100
        sigma_rho.append(sigma)
    return sigma_rho

for i in range(3):
    rho_lit_broj = rho_lit_lista[i][1]
    lista_sigma_rho = pogreska_gustoca(rho_sredina_lista, rho_lit_broj)
    najmanji_sigma_rho = min(lista_sigma_rho) #vraca najmanju pogresku gustoce
    for j in range(3):
        if najmanji_sigma_rho == lista_sigma_rho[j]:
            print(f'Valjak {j+1} je {rho_lit_lista[i][0]}\nPogreska gustoce iznosi {najmanji_sigma_rho} %')