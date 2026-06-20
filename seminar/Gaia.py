# Izbrojite koliko zvijezda vidimo na noćnom nebu s lokacije našeg 
# Fakulteta koristeći podatke Gaia satelita.
import numpy as np
from astropy.io import fits

with fits.open('gaia.fits') as hdul: 
    # open vraća PyFITS objekt pod nazivom data_gaia
    # lista (array) slična python listama koja se sastoji od HDU(heather data unit) objekata
    # biranjem data[0] indeksa se oznacava primarni HDU
    data = hdul[1].data # biranjem data_gaia[1] indeksa oznacava se sekundarni HDU u kojem su podatci o zvijezdama
    # preko prije provjerenih .columns vadim pojedine kao liste za daljnje korištenje
    ID = data['source_id']
    ra_deg = data['ra']
    dec_deg = data['dec']
    mag = data['phot_g_mean_mag']

# skup podataka data ima 4 stupca:
# 1. source_id - jedinstveni broj svake zvijezde - K: 64-bitni int tip podataka
# globalni nebeski koordinatni sustav
# 2. ra - right ascension - udaljenost objekta od proljetne ravnodnevnice - D: Double precision float (64-bit)
# 3. dec - declination - udaljenost objekta sjeverno ili južno od nebeskog ekvatora - D - unit deg - stupnjevi
# 4. phot_g_mean_mag - predstavlja prosječnu prividnu svjetlinu nebeskog objekta u - E: Single precision float (32-bit)
# Gaia G fotometrijskom pojasu, izračunatu iz srednjeg fluksa i pretvorenu u Veginu skalu magnitude


# zbog rotacije zemlje ra je ovisan o satu dana

# SVE ZVIJEZDE VIDLJIVE PREKO GODINE
# zvijezde kruže svako 24 sata, tkd. je RA u rangeu od 0 do 24h
# Dec ovisi o zemljopisnoj širini lat
# min_dec = lat - 90° <-- naša vidljivost 
# max_dec = lat + 90° 
# (naravno zvijezde ne mogu ici izvan zvjezdanih polova, rezultat treba biti između -90 i 90° )

ra = np.radians(ra_deg)
dec = np.radians(dec_deg)

# vidljivost se temelji na magnitudi 
# minimalna magnituda vidljivosti je 6.5, ali zbog svjetlosnog onečišćenja može pasti na čak 4 ili 3
eye_mag = [3.5, 4.5, 5.5, 6.5]

lat_deg = 43.512140407590124 #°
lat = np.radians(lat_deg)
min_dec = np.radians(lat_deg - 90) #°

# boolean array - array koji se sastoji samo od True i False
# mogu se postaviti uvjeti koji ce jednostavno odrediti jesu li elementi array-a istiniti ili ne
uvjet_dec = dec > min_dec

def godisnji_broj(mag, eye_mag, uvjet_dec): #staviti indeksiranu magnitudu vidljivosti
    uvjet_mag = mag < eye_mag
    uvjeti_godisnji = uvjet_dec & uvjet_mag #kombinira booleane
    broj_godisnji = np.sum(uvjeti_godisnji) # zbraja sve True elemnte booleana
    return broj_godisnji
#print(f'Godišnje iznad Prirodoslovno-matematičkog fakulteta vidljivo je {broj_godisnji} zvijezda.') prepravit za rezultate


#for i in np.arange(min_dec, 90): #° 
#    for d in data_gaia[1].data['dec']: #svaki element u list
#        if i == d: #svaki element koji se poklapa s parametrom
#            indeksi_dec.append(data_gaia[1].data['dec'].index(d)) 
#            #ovi indeksi ce se poklapati sa indeksima u bilo kojim drugim stupcima

#magnituda_lista = []
#for i in indeksi_dec:
#    magnituda_lista.append(data_gaia[1].data['phot_g_mean_mag'][i])

#for m in magnituda_lista:
#    if m < eye_mag_max:
#        brojac_godisnji += 1





# SVE ZVIJEZDE VIDLJIVE U ODREĐENOM VREMENU 
# Dec ostaje isti kao prije
# KALKULACIJA RA:
# 1. Odrediti vrijeme - zadano na nocnom nebu - u ponoc 25. lipnja 2024
# Local Median  Sidereal Time - lokalno zvjezdano vrijeme - preko longditude - zemljopisne duzine
# lon = 16.46849379527058° = 16° 28' 6.57766"
# LST = 19 h 20 min 22.8 s = 19.33967 h
# LST = 290° 5' 43'' = 290.0952° izracunato preko online kalkulatora
# 2. hour angle HA = LST - RA  
# altitude - visina (a)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(HA)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(LST - RA )
# zvijezda je vidljiva ako je sin(a) >= 0 

LST = 290.0952 #°


def trenutni_broj(mag, lat, dec, ra, LST, eye_mag, uvjet_dec): #staviti indeksiranu magnitudu vidljivosti
    LSTr = np.radians(LST)
    sin_a = np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(LSTr - ra)
    uvjet_ra = sin_a >= 0
    uvjet_mag = mag < eye_mag
    uvjeti = uvjet_dec & uvjet_mag & uvjet_ra #kombinira booleane
    broj = np.sum(uvjeti) # zbraja sve True elemnte booleana
    return broj



#print(f'Na ovaj dan (25.6.) 2024. godine u ponoć bilo je vidljivo {broj_ponoc} zvijezda.')
# prepravit

# SVE ZVIJEZDE VIDLJIVE PREKO NOĆI 25.6.2024. - 26.6.2024.
# Slično kao izračun za sve zvijezde u određenom vremenu
# uzima se početna i krajnja točka, tj. vrijeme zalaska i izlaska sunca
# zvijezde prikazane u ta dva trenutka prekrivaju sve zvijezde vidljive tijekom noći
# potrebno je obratiti pozornost na prostor gdje se horizonti za ta dva vremena sijeku
# kako ne bi prikazali zvijezde u toj točci dvaput - to su zvijezde koje se vide cijelu noć

# M + N = 2L + zbroj_bezL ---> potreban rezultat je L + zbroj_bezL

LST_dan = [['zalazak', 240.6932], ['izlazak', 10.0464]] #° -> 20h 39min, 5h 15min

def nocni_broj(mag, lat, dec, ra, LST_dan, eye_mag, uvjet_dec):
    lst_zalazak = LST_dan[0][1]
    lst_izlazak = LST_dan[1][1]

    if lst_izlazak < lst_zalazak: #kasnije pomaže u određivanju aproksimacije lst preko noći
        lst_izlazak += 360 #° kako bi izlazak mogao biti zavrsni LST mora imati veci iznos od zalaska

    lst_noc = np.linspace(lst_zalazak, lst_izlazak, num = 50) #ravnomjerno raspoređeni koraci
    #aproksimira lst za 50 puta preko noci
    #pošto su arrays kao matriksi, za izvedbu (lst - ra) oba arraya ne smiju biti samo redovi
    #moraju biti red i stupac kako se ne bi oduzimali samo elementi u parovima
    #već bi se od svake vrijednosti lst oduzela svaka vrijednost ra
    lst_noc_rad = np.radians(lst_noc).reshape(1, -1) #pretvara lst_noc_rad u 2D matricu od jednog redka 
    #ostale vrijednosti se pretvaraju u stupce
    ra_stupac = ra.reshape(-1, 1)
    dec_stupac = dec.reshape(-1, 1)

    sin_a = np.sin(lat) * np.sin(dec_stupac) + np.cos(lat) * np.cos(dec_stupac) * np.cos(lst_noc_rad - ra_stupac)

    #np.any testira je element u array-u True na određenoj osi
    #tj. pošto je rezultat sin_a sada matrica, np.any gleda je li u pojedinom redu iti jednom uvjet ispunjen
    #ako je uvjet jednom ispunjen, np.any zapisuje True
    #tako se zvijezde koje više puta u noći ispunjuju uvjet zapisuju samo jednom

    uvjet_ra = np.any(sin_a >= 0, axis = 1) #axis 1 promatra horizontalnu os, tj redak
    uvjet_mag = mag < eye_mag
    uvjeti = uvjet_dec & uvjet_mag & uvjet_ra
    broj = np.sum(uvjeti)
    return broj

print(nocni_broj(mag, lat, dec, ra, LST_dan, eye_mag[3], uvjet_dec), trenutni_broj(mag, lat, dec, ra, LST, eye_mag[3], uvjet_dec), godisnji_broj(mag, eye_mag[3], uvjet_dec))

#zbog uvjet_dec stalno vraca istu vrijednost