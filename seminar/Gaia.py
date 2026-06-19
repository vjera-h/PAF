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
    ra = data['ra']
    dec = data['dec']
    mag = data['phot_g_mean_mag']

# skup podataka data ima 4 stupca:
# 1. source_id - jedinstveni broj svake zvijezde - K: 64-bitni int tip podataka
# globalni nebeski koordinatni sustav
# 2. ra - right ascension - udaljenost objekta od proljetne ravnodnevnice - D: Double precision float (64-bit)
# 3. dec - declination - udaljenost objekta sjeverno ili južno od nebeskog ekvatora - D - unit deg - stupnjevi
# 4. phot_g_mean_mag - predstavlja prosječnu prividnu svjetlinu nebeskog objekta u - E: Single precision float (32-bit)
# Gaia G fotometrijskom pojasu, izračunatu iz srednjeg fluksa i pretvorenu u Veginu skalu magnitude


# vidljivost se temelji na magnitudi - u prosjeku maksimalna magnituda je 6.5
# NISAM SIGURNA JE LI OVO TOČNO, TREBAM LI BIT SPECIFIČNIJA ZA SPLIT??

# zbog rotacije zemlje ra je ovisan o satu dana

# SVE ZVIJEZDE VIDLJIVE PREKO GODINE
# zvijezde kruže svako 24 sata, tkd. je RA u rangeu od 0 do 24h
# Dec ovisi o zemljopisnoj širini lat
# min_dec = lat - 90° <-- naša vidljivost 
# max_dec = lat + 90° 
# (naravno zvijezde ne mogu ici izvan zvjezdanih polova, rezultat treba biti između -90 i 90° )

eye_mag_max = 6.5

lat = 43.512140407590124 #°
min_dec = lat - 90 #°
brojac_godisnji = 0
indeksi_dec = []

# boolean array - array koji se sastoji samo od True i False
# mogu se postaviti uvjeti koji ce jednostavno odrediti jesu li elementi array-a istiniti ili ne
uvjet_dec = dec > min_dec
uvjet_mag = mag < eye_mag_max

uvjeti_godisnji = uvjet_dec & uvjet_mag #kombinira booleane

broj_godisnji = np.sum(uvjeti_godisnji) # zbraja sve True elemnte booleana

print(f'Godišnje iznad Prirodoslovno-matematičkog fakulteta vidljivo je {broj_godisnji} zvijezda.')


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
# lon = 16.46849379527058°
# LST = 19 h 20 min 22.8 s = 19.33967 h
# LST = 290° 5' 43'' = 290.0952° izracunato preko online kalkulatora
# 2. hour angle HA = LST - RA 
# altitude - visina (a)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(HA)
# sin(a) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(LST - RA )
# zvijezda je vidljiva ako je sin(a) >= 0 

LST = 290.0952 #°
sin_a = np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(LST - ra)

uvjet_ra = sin_a >= 0

uvjet_ponoc = uvjet_dec & uvjet_mag & uvjet_ra

broj_ponoc = np.sum(uvjet_ponoc)

print(f'Na ovaj dan (25.6.) 2024. godine u ponoć bilo je vidljivo {broj_ponoc} zvijezda.')