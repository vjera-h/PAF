# Izbrojite koliko zvijezda vidimo na noćnom nebu s lokacije našeg 
# Fakulteta koristeći podatke Gaia satelita.
import numpy as np
from astropy.io import fits

with fits.open('gaia.fits') as hdul: 
    # open vraća PyFITS objekt pod nazivom data_gaia
    # lista slična python listama (array) koja se sastoji od HDU(heather data unit) objekata
    # biranjem hdul[0] indeksa se oznacava primarni HDU
    data = hdul[1].data # biranjem hdul[1] indeksa oznacava se sekundarni HDU u kojem su podatci o zvijezdama
    # preko prije provjerenih .columns vadim pojedine stupce kao liste za daljnje korištenje
    ID = data['source_id']
    ra_deg = data['ra']
    dec_deg = data['dec']
    mag = data['phot_g_mean_mag']

# Skup podataka data ima 4 stupca:
# 1. source_id - jedinstveni broj svake zvijezde - K: 64-bitni int tip podataka
# globalni nebeski koordinatni sustav
# 2. ra - right ascension - udaljenost objekta od proljetne ravnodnevnice - D: Double precision float (64-bit) - unit deg - stupnjevi
# 3. dec - declination - udaljenost objekta sjeverno ili južno od nebeskog ekvatora - D - unit deg - stupnjevi
# 4. phot_g_mean_mag - predstavlja prosječnu prividnu svjetlinu nebeskog objekta u - E: Single precision float (32-bit)
# Gaia G fotometrijskom pojasu, izračunatu iz srednjeg fluksa i pretvorenu u Veginu skalu magnitude


# zbog rotacije zemlje ra je ovisan o datumu i satu dana

# SVE ZVIJEZDE VIDLJIVE PREKO GODINE
# zvijezde kruže svako 24 sata, RA je u rangeu od 0 do 24h - irelevantan pošto se u godini prolazi svaki RA
# Dec ovisi o zemljopisnoj širini - lat
# min_dec = lat - 90° <-- naša vidljivost 
# max_dec = lat + 90° 
# (naravno zvijezde ne mogu ići izvan zvjezdanih polova, rezultat treba biti između -90° i 90° )

ra = np.radians(ra_deg)
dec = np.radians(dec_deg)

# vidljivost se temelji na magnitudi 
# maksimalna magnituda vidljivosti je 6.5, ali zbog svjetlosnog onečišćenja može pasti na čak 4 ili 3
# što je zvijezda svjetlija, to joj je manja magnituda
eye_mag = [3.5, 4.5, 5.5, 6.5]

lat_deg = 43.512140407590124 #°
lat = np.radians(lat_deg)
min_dec = np.radians(lat_deg - 90) #°


def godisnji_broj(mag, eye_mag, dec, min_dec): # potrebno staviti indeksiranu magnitudu 
    # boolean array - array koji se sastoji samo od True i False
    # mogu se postaviti uvjeti koji će jednostavno odrediti jesu li elementi array-a istiniti ili ne
    uvjet_dec = dec > min_dec
    uvjet_mag = mag < eye_mag
    uvjeti_godisnji = uvjet_dec & uvjet_mag # kombinira booleane - istiniti su sao oni kojima su oba uvjeta istinita 
    broj_godisnji = np.sum(uvjeti_godisnji) # zbraja sve True elemnte booleana
    return broj_godisnji


# SVE ZVIJEZDE VIDLJIVE U ODREĐENOM VREMENU 
# min_dec ostaje isti kao prije pošto se ne mijenja geografska širina
# KALKULACIJA RA:
# 1. Odrediti vrijeme - zadano na nocnom nebu - u ponoc različitih datuma
# Local Median  Sidereal Time - lokalno zvjezdano vrijeme - preko longditude - zemljopisne duzine
# lon = 16.46849379527058° = 16° 28' 6.57766"
# izracunato preko online kalkulatora:
#   LST = 290° 5' 43'' = 290.0952° za 25. lipnja 2024
#   LST = 189° 33' 33'' = 189.5590° za 15. ožujka 2024
#   LST = 17° 59' 41'' = 17.9948° za 23. rujna 2015
#   LST = 86° 46' 56'' = 86.7823° za 1. prosinca 2020
# 2. hour angle HA = LST - RA  
# koordinatni sustav altitude/azimuth 
# biran je altitude - visina (a)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(HA)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(LST - RA )
# zvijezda je vidljiva ako je sin(a) >= 0 

LST = [['25. lipnja 2024', 290.0952],['15. ozujka 2024', 189.5590], ['23. rujna 2023', 17.9948], ['1. prosinca 2020', 86.7823]] #° (ponoc)


def trenutni_broj(mag, lat, dec, ra, min_dec, LST, eye_mag): # staviti indeksiranu magnitudu vidljivosti i LST pri pozivanju funkcije
    filter_mag = mag < eye_mag 
    # filtriranje znaci da opstaju samo elementi arraya koji imaju isti index kao True u filter_mag
    # potrebno kako se bi se račun smanjio sa 3mil na samo one koje ispunjuju uvjet magnitude
    fil_ra = ra[filter_mag]
    fil_dec = dec[filter_mag]
    
    LSTr = np.radians(LST)
    sin_a = np.sin(lat) * np.sin(fil_dec) + np.cos(lat) * np.cos(fil_dec) * np.cos(LSTr - fil_ra)
    uvjet_ra = sin_a >= 0 # nije potreban uvjet_mag pošto je taj dio zvijezda već filtriran
    uvjet_dec = fil_dec > min_dec
    broj = np.sum(uvjet_ra & uvjet_dec) # zbraja sve True elemnte booleana
    return broj

# SVE ZVIJEZDE VIDLJIVE PREKO NOĆI 
# Slično kao izračun za sve zvijezde u određenom vremenu
# uzima se početna i krajnja točka, tj. vrijeme zalaska i izlaska sunca
# kako bi se mogle zbrojiti sve zvijezde koje se pojave preko noći potrebno je puno više vremena od samog zalaska i izlaska
# npr. neke zvijezde se mogu pojaviti samo od 1h do 3h
# zato se ostatak vremena aproksimira i provjerava

# vrijeme izlaska i zalaska sunca za određene datume je pronađeno na internetu
LST_dan = [['25. - 26.6.2024.', [['zalazak', 240.6932], ['izlazak', 10.0464]]], #° -> 20h 39min, 5h 15min
           ['15. - 16.3.2024.', [['zalazak', 100.5491], ['izlazak', 281.7939]]], #° -> 18h 1min, 6h 4min
           ['23. - 24.9.2015.', [['zalazak', 301.5190], ['izlazak', 119.0207]]], #° -> 18h 51min, 6h 43min
           ['1. - 2.12.2015.', [['zalazak',  332.2024], ['izlazak', 195.3116]]]] #° -> 16h 19min, 7h 9min

def nocni_broj(mag, lat, dec, ra, min_dec, LST_dan, eye_mag):
    lst_zalazak = LST_dan[0][1]
    lst_izlazak = LST_dan[1][1]

    if lst_izlazak < lst_zalazak: # kasnije pomaže u određivanju aproksimacije lst preko noći
        lst_izlazak += 360 #° kako bi izlazak mogao biti zavrsni LST mora imati veci iznos od zalaska

    lst_noc = np.linspace(lst_zalazak, lst_izlazak, num = 50) # ravnomjerno raspoređeni koraci
    # aproksimira lst za 50 puta preko noci
    # pošto su arrays kao matriksi, za izvedbu (lst - ra) oba arraya ne smiju biti samo redovi --> oduzimanje elementa istog indeksa
    # moraju biti red i stupac kako bi se od svake vrijednosti lst oduzela svaka vrijednost ra
    lst_noc_rad = np.radians(lst_noc).reshape(1, -1) # reshape pretvara lst_noc_rad u 2D matricu od jednog redka 

    filter_mag = mag < eye_mag # ponovno filtriranje prema magnitudi

    fil_ra = ra[filter_mag]
    fil_dec = dec[filter_mag]
    
    # ostale vrijednosti .reshape pretvara u stupce
    ra_stupac = fil_ra.reshape(-1, 1)
    dec_stupac = fil_dec.reshape(-1, 1)

    sin_a = np.sin(lat) * np.sin(dec_stupac) + np.cos(lat) * np.cos(dec_stupac) * np.cos(lst_noc_rad - ra_stupac)

    # np.any testira je li element u array-u True na određenoj osi
    # tj. pošto je rezultat sin_a sada matrica, np.any gleda je li u pojedinom redu iti jednom uvjet ispunjen
    # ako je uvjet jednom ispunjen, np.any zapisuje True
    # tako se zvijezde koje više puta u noći ispunjuju uvjet zapisuju samo jednom

    uvjet_ra = np.any(sin_a >= 0, axis = 1) # axis 1 promatra horizontalnu os, tj redak - vraća 1D niz
    uvjet_dec = fil_dec > min_dec

    broj = np.sum(uvjet_ra & uvjet_dec)
    return broj

print('-'*100)
print('VIDLJIVOST ZVIJEZDA IZNAD LOKACIJE PRIRODOSLOVNO-MATEMATIČKOG FAKULTETA SPLIT')
print('-'*100)
print(f'-Ovo su mjerenja za viljivost golim okom maksimalne magnitude {eye_mag[0]}-')
print(f'Godišnje se vidi {godisnji_broj(mag, eye_mag[0], dec, min_dec)} zvijezda.')
print(f'Broj zvijezda u trenutku 00h 00min 00sec:\n datuma {LST[0][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[0][1], eye_mag[0])}\n datuma {LST[1][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[1][1], eye_mag[0])}\n datuma {LST[2][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[2][1], eye_mag[0])}\n datuma {LST[3][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[3][1], eye_mag[0])} ')
print(f'Ukupni broj zvijezda tijekom noći:\n {LST_dan[0][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[0][1], eye_mag[0])}\n {LST_dan[1][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[1][1], eye_mag[0])}\n {LST_dan[2][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[2][1], eye_mag[0])}\n {LST_dan[3][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[3][1], eye_mag[0])}')

print('-'*100)
print(f'-Ovo su mjerenja za viljivost golim okom maksimalne magnitude {eye_mag[1]}-')
print(f'Godišnje se vidi {godisnji_broj(mag, eye_mag[1], dec, min_dec)} zvijezda.')
print(f'Broj zvijezda u trenutku 00h 00min 00sec:\n datuma {LST[0][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[0][1], eye_mag[1])}\n datuma {LST[1][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[1][1], eye_mag[1])}\n datuma {LST[2][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[2][1], eye_mag[1])}\n datuma {LST[3][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[3][1], eye_mag[1])} ')
print(f'Ukupni broj zvijezda tijekom noći:\n {LST_dan[0][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[0][1], eye_mag[1])}\n {LST_dan[1][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[1][1], eye_mag[1])}\n {LST_dan[2][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[2][1], eye_mag[1])}\n {LST_dan[3][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[3][1], eye_mag[1])}')

print('-'*100)
print(f'-Ovo su mjerenja za viljivost golim okom maksimalne magnitude {eye_mag[2]}-')
print(f'Godišnje se vidi {godisnji_broj(mag, eye_mag[2], dec, min_dec)} zvijezda.')
print(f'Broj zvijezda u trenutku 00h 00min 00sec:\n datuma {LST[0][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[0][1], eye_mag[2])}\n datuma {LST[1][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[1][1], eye_mag[2])}\n datuma {LST[2][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[2][1], eye_mag[2])}\n datuma {LST[3][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[3][1], eye_mag[2])} ')
print(f'Ukupni broj zvijezda tijekom noći:\n {LST_dan[0][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[0][1], eye_mag[2])}\n {LST_dan[1][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[1][1], eye_mag[2])}\n {LST_dan[2][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[2][1], eye_mag[2])}\n {LST_dan[3][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[3][1], eye_mag[2])}')

print('-'*100)
print(f'-Ovo su mjerenja za viljivost golim okom maksimalne magnitude {eye_mag[3]}-')
print(f'Godišnje se vidi {godisnji_broj(mag, eye_mag[3], dec, min_dec)} zvijezda.')
print(f'Broj zvijezda u trenutku 00h 00min 00sec:\n datuma {LST[0][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[0][1], eye_mag[3])}\n datuma {LST[1][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[1][1], eye_mag[3])}\n datuma {LST[2][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[2][1], eye_mag[3])}\n datuma {LST[3][0]}: {trenutni_broj(mag, lat, dec, ra, min_dec, LST[3][1], eye_mag[3])} ')
print(f'Ukupni broj zvijezda tijekom noći:\n {LST_dan[0][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[0][1], eye_mag[3])}\n {LST_dan[1][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[1][1], eye_mag[3])}\n {LST_dan[2][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[2][1], eye_mag[3])}\n {LST_dan[3][0]}: {nocni_broj(mag, lat, dec, ra, min_dec, LST_dan[3][1], eye_mag[3])}')
