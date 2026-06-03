#tri oblika standardne devijacije u obreadi podataka

import numpy as np

# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa ]
malo_n = [99.8 , 100.1 , 99.9 , 100.2 , 100.0]

# 10000 mjerenja istog eksperimenta ( simulacija )
np.random.seed(42)
veliko_n = np.random.normal( loc =100.0 , scale =0.2 , size =10000).tolist()

def aritmeticka_sredina(brojevi):
    n = len(brojevi)
    sredina = sum(brojevi) / n
    return sredina

def devijacija_n(lista):
    #sigma_n = sqrt(sum((xi -avg_x)^2) / n)
    n = len(lista)
    x_avg = aritmeticka_sredina(lista)
    razlika_lista = []
    for x in lista:
        razlika = (x - x_avg)**2
        razlika_lista.append(razlika)
    sigma_n = np.sqrt(sum(razlika_lista)/n)
    return sigma_n

def devijacija_s(lista):
    #s = sqrt(sum((xi -avg_x)^2) / n - 1)
    n = len(lista)
    x_avg = aritmeticka_sredina(lista)
    razlika_lista = []
    for x in lista:
        razlika = (x - x_avg)**2
        razlika_lista.append(razlika)
    s = np.sqrt(sum(razlika_lista)/(n -  1))
    return s

def devijacija_x(lista):
    #sigma_x = s / sqrt(n)
    n = len(lista)
    return devijacija_s(lista) / np.sqrt(n)

def relativna_razlika(a, b):
    #rel_raz = abs(a - b)/((a+b)/2) * 100
    absol = abs(a - b)
    nazivnik = (a + b)/2
    return absol / nazivnik * 100


# za malo n
mala_devijacija_n = devijacija_n(malo_n)
mala_devijacija_s = devijacija_s(malo_n)
mala_devijacija_x = devijacija_x(malo_n)

# za veliko n
velika_devijacija_n = devijacija_n(veliko_n)
velika_devijacija_s = devijacija_s(veliko_n)
velika_devijacija_x = devijacija_x(veliko_n)

print(f'Za  s:\nmali broj n: {mala_devijacija_s}, veliki broj n: {velika_devijacija_s}')
print(f'Za x-bar:\nmali broj n: {mala_devijacija_x}, veliki broj n: {velika_devijacija_x}')
#s povećanjem broja n devijacija s je veća
#s povećanjem broja n devijacija x-bar je manja

mala_relativna_razlika = relativna_razlika(mala_devijacija_n, mala_devijacija_s)
velika_relativna_razlika = relativna_razlika(velika_devijacija_n, velika_devijacija_s)

print(f'Relativna razlika za mali n: {mala_relativna_razlika}')
print(f'Relativna razlika za veliki n: {velika_relativna_razlika}')
#relativna razlika za mali n je znatno veća od relativne razlike za veliki n

print(f'Devijacija s python np.std() je:\nza mali n {np.std(malo_n)}\nza veliki n {np.std(veliko_n)}')
print(f'Devijacija s devijecijom n je:\nza mali n {mala_devijacija_n}\nza veliki n {velika_devijacija_n}')