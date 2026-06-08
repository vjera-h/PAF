#Masa zvijezde Sirius A određena je 60 puta iz analize spektroskopske binarne zvijezde 
# (mjerenje radijalne brzine i orbitalni parametri). 
# Većina mjerenja prati normalnu razdiobu oko prave vrijednosti,
# ali nekoliko sadrži grube pogreške pri redukciji podataka.

import numpy as np

np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] 
# pogreske pri redukciji podataka

#Napišite funkciju histogram(podaci, k) koja prima listu mjerenja i broj razreda k te:

def histogram(podaci, k):
    #(a) izračuna širinu razreda h prema formuli (2) i rubove svakog razreda,
    minimum = min (podaci)
    maksimum = max(podaci)
    h = (maksimum - minimum) / k

    #rubovi - od minimuma do k r korakom od h
    rubovi = []
    for i in range(k + 1): #treba bit od 0 do k sa ukljucenim k da bi se mogli odrediti sve frekvencije
        rub = minimum + i * h
        rubovi.append(rub)
    
    #(b) prebroji koliko podataka pada u svaki razred
    #prebrojit podatke između dva susjedna ruba [x_{i-1}, x_i): frekvencija

    frekvencije = []

    for i in range(k):
        x_ = rubovi[i]
        x_i = rubovi[i + 1] #izbjegava da je x_ zadnji element liste [-1]

        frek = 0
        for p in podaci:
            if p >= x_ and p <x_i:
                frek += 1
            elif i == k - 1 and p == x_i:
                frek += 1

        frekvencije.append(frek)

        #ispiše histogram u tekstualnom obliku [x_{i-1}, x_i): frekvencija

        print(f'[{x_:.3f}, {x_i:.3f}) : {frekvencije[i]}') #:.3f ispisuje 3 decimale
    
    return h, rubovi, frekvencije

# Pozovite funkciju za mase_ciste s k = 10 razreda 
# i nacrtajte dobiveni histogram koristeći matplotlib.pyplot.bar() 
# s ručno izračunatim rubovima i frekvencijama. 
# Zadnji razred mora uključivati i maksimalnu vrijednost. 
# Dodajte oznake osi i naslov.
import matplotlib.pyplot as plt

k = 10

h, rubovi, frekvencije = histogram(mase_ciste, k)

plt.bar(rubovi[:-1], frekvencije, width = h, align='edge', edgecolor='black')
#rubovi su gdje pocinje svaki stupac, izbacen je zadnji jer ih ima 11, a ima 10 frekvencija
#frekvencije su visine stupaca
#align = 'edge' poravnavanje lijevih rubova stupaca s xom
plt.xlabel('Masa')
plt.ylabel('Frekvencije')
plt.title('Histogram prema funkciji')
plt.tight_layout()
plt.grid(True)
plt.show()

# Nacrtajte histogram podataka mase_ciste koristeći gotovi modul. 
# Koristite k = 10 razreda i usporedite dobivene frekvencije s rezultatima Zadatka 1. 
# Na isti graf ucrtajte vertikalnu liniju na poziciji aritmetičke sredine i medijana. 

plt.hist(mase_ciste, bins = 10, edgecolor = 'black')
plt.xlabel('Masa')
plt.ylabel('Frekvencije')
plt.title('Histogram prema gotovom modulu - 10 razreda')
plt.axvline(np.mean(mase_ciste), linestyle = '-', color = 'pink', label = 'Aritmeticka sredina')
plt.axvline(np.median(mase_ciste), linestyle = '--', color = 'purple', label = 'Medijan')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

# Isprobajte kako izgleda graf kada promijenite broj razreda.

plt.hist(mase_ciste, bins = 5, edgecolor = 'black')
plt.xlabel('Masa')
plt.ylabel('Frekvencije')
plt.title('Histogram prema gotovom modulu - 5 razreda')
plt.axvline(np.mean(mase_ciste), linestyle = '-', color = 'pink', label = 'Aritmeticka sredina')
plt.axvline(np.median(mase_ciste), linestyle = '--', color = 'purple', label = 'Medijan')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

# Napišite funkciju medijan(podaci) koja računa medijan prema formuli (1) 
# bez korištenja gotovih modula (sorted() je dopušten). 
# Testirajte funkciju na dva primjera:

a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6] # paran n
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5] # neparan n

def medijan(podaci):
    n = len(podaci)
    pod = sorted(podaci)
    if n % 2 != 0: #n neparan x(n +1)/2
        x = int(((n + 1)/2)-1) #- 1 zato sta ako trazimo npr 5. element u listi, trebamo napisati 4
        x_tilda = pod[x] #lista ide od 0 do n-1


    else: #n paran (x(n/2) + x((n/2) + 1))/2
        x_1 = int((n/2)-1)
        x_2 = int(((n/2) + 1)-1)
        x_tilda = (pod[x_1] + pod[x_2])/2

    return x_tilda

print('='*50)
print(f'Medijan za listu a: {medijan(a)}\nMedijan za listu b: {medijan(b)}')

#Za skup mase izračunajte aritmetičku sredinu i medijan te ispišite razliku između njih. 

def aritmeticka_sredina(brojevi):
    n = len(brojevi)
    sredina = sum(brojevi) / n
    return sredina

arit_mase = aritmeticka_sredina(mase)
medij_mase = medijan(mase)

print('='*50)
print(f'Razlika između aritmetičke sredine mase {arit_mase} i medijana {medij_mase} je:\n{arit_mase-medij_mase}')

# Uklonite vrijednosti koje značajno odstupaju od mjerenja i ponovite izračun.
# IQR (Interquartile Range) method
# tehnika koja otkriva outliere mjerenjem varijabilnosti u skupu podataka 

uklonjene_mase = sorted(mase)

Q1 = np.percentile(uklonjene_mase, 25, interpolation = 'midpoint') 
Q2 = np.percentile(uklonjene_mase, 50, interpolation = 'midpoint') 
Q3 = np.percentile(uklonjene_mase, 75, interpolation = 'midpoint') 
# izracunava neki percentil(polozaj nekog podatka u odnosu na cijeli skup) 
# podataka duž određene osi

IQR = Q3 - Q1

donja_granica = Q1 - 1.5 * IQR
gornja_granica = Q3 + 1.5 * IQR

uklonjene_mase = [uk for uk in mase if donja_granica < uk < gornja_granica]


arit_uk_mase = aritmeticka_sredina(uklonjene_mase)
medij_uk_mase = medijan(uklonjene_mase)

print('='*50)
print('Za mase bez vrijednosti koje znčajno odstupaju od mjerenja ')
print(f'Razlika između aritmetičke sredine mase {arit_uk_mase} i medijana {medij_uk_mase} je:\n{arit_uk_mase-medij_uk_mase}')

# Za koliko se promijenila srednja vrijednost, a za koliko medijan? 
print('='*50)
print(f'Razlika između aritmetičkih sredina mase je:\n{arit_mase} - {arit_uk_mase} = {arit_mase - arit_uk_mase}')
print(f'Razlika između medijana je:\n{medij_mase} - {medij_uk_mase} = {medij_mase - medij_uk_mase}')
#srednja vrijednost se dosta znacajno promijenila, dok se medijan promijenio vrlo malo

# Na jedan graf ucrtajte histogram svih mjerenja te sve četiri vertikalne linije 
# (srednja i medijan sa i bez pogrešnih mjerenja). 

plt.hist(mase, bins = 15, edgecolor = 'black')
plt.xlabel('Masa')
plt.ylabel('Frekvencije')
plt.axvline(arit_mase, linestyle = '-', color = 'pink', label = 'Aritmeticka sredina')
plt.axvline(arit_uk_mase, linestyle = '--', color = 'purple', label = 'Aritmeticka sredina bez znacajnih odstupanja')
plt.axvline(medij_mase, linestyle = '-.', color = 'green', label = 'Medijan')
plt.axvline(medij_uk_mase, linestyle = ':', color = 'cyan', label = 'Medijan bez znacajnih odstupanja')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
# Što ovaj rezultat govori o tome koja veličina bolje procjenjuje pravu masu zvijezde?
# Pravu masu zvijezde bolje procjenjuje medijan ako ima znacajnih odstupanja u mjerenju, 
# ali kada nema znacajnih odstupanja aritmeticka sredina je preciznija.