import numpy as np
from astropy.io import fits

with fits.open('gaia.fits') as hdul: 
    data = hdul[1].data 
    ID = data['source_id']
    ra_deg = data['ra']
    dec_deg = data['dec']
    mag = data['phot_g_mean_mag']

ra = np.radians(ra_deg)
dec = np.radians(dec_deg)

eye_mag = [3.5, 4.5, 5.5, 6.5]

lat_deg = 43.512140407590124 #°
lat = np.radians(lat_deg)
min_dec = np.radians(lat_deg - 90) #°


def godisnji_broj(mag, eye_mag, dec, min_dec):
    uvjet_dec = dec > min_dec
    uvjet_mag = mag < eye_mag
    uvjeti_godisnji = uvjet_dec & uvjet_mag 
    broj_godisnji = np.sum(uvjeti_godisnji)
    return broj_godisnji

LST = [['25. lipnja 2024', 290.0952],['15. ozujka 2024', 189.5590], ['23. rujna 2023', 17.9948], ['1. prosinca 2020', 86.7823]] #° (ponoc)


def trenutni_broj(mag, lat, dec, ra, min_dec, LST, eye_mag): 
    filter_mag = mag < eye_mag  
    fil_ra = ra[filter_mag]
    fil_dec = dec[filter_mag]
    
    LSTr = np.radians(LST)
    sin_a = np.sin(lat) * np.sin(fil_dec) + np.cos(lat) * np.cos(fil_dec) * np.cos(LSTr - fil_ra)
    uvjet_ra = sin_a >= 0
    uvjet_dec = fil_dec > min_dec
    broj = np.sum(uvjet_ra & uvjet_dec) 
    return broj

LST_dan = [['25. - 26.6.2024.', [['zalazak', 240.6932], ['izlazak', 10.0464]]], #°
           ['15. - 16.3.2024.', [['zalazak', 100.5491], ['izlazak', 281.7939]]], #° 
           ['23. - 24.9.2015.', [['zalazak', 301.5190], ['izlazak', 119.0207]]], #° 
           ['1. - 2.12.2015.', [['zalazak',  332.2024], ['izlazak', 195.3116]]]] #° 

def nocni_broj(mag, lat, dec, ra, min_dec, LST_dan, eye_mag):
    lst_zalazak = LST_dan[0][1]
    lst_izlazak = LST_dan[1][1]

    if lst_izlazak < lst_zalazak: 
        lst_izlazak += 360 #° 

    lst_noc = np.linspace(lst_zalazak, lst_izlazak, num = 50) 
    lst_noc_rad = np.radians(lst_noc).reshape(1, -1) 

    filter_mag = mag < eye_mag 

    fil_ra = ra[filter_mag]
    fil_dec = dec[filter_mag]
    
    ra_stupac = fil_ra.reshape(-1, 1)
    dec_stupac = fil_dec.reshape(-1, 1)

    sin_a = np.sin(lat) * np.sin(dec_stupac) + np.cos(lat) * np.cos(dec_stupac) * np.cos(lst_noc_rad - ra_stupac)

    uvjet_ra = np.any(sin_a >= 0, axis = 1)
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
