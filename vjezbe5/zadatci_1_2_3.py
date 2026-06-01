# (a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? 
# Koji rezultat dobijete koristeći Python? Objasnite
print(5.0 - 4.935)
#Koristeći python rezultat je 5.0 - 4.935 = 0.06500000000000039

# (b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. 
# Objasnite rezultat koji ste dobili.
print(0.1 + 0.2 + 0.3)
# Koristeći python rezultat je 0.1 + 0.2 + 0.3 = 0.6000000000000001

# Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 
# pa zatim N puta oduzima 1/3 broju 5.
# Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. 
# Objasnite rezultat koji ste dobili.

N1 = 200
N2 = 2000
N3 = 20000

def operacije(N):
    broj = 5
    for i in range(0, N):
        broj += 1/3
    for i in range(0, N):
        broj -= 1/3
    rezultat = print(f'Za N = {N}:\nOvo je rezultat {broj}')

operacije(N1)
operacije(N2)
operacije(N3)

# Float brojevi u pythonu su aproksimacija realnih brojeva, ne istiniti realni brojevi.
# Može se pohraniti samo ograničen broj znamenki, 
# što dovodi do pogrešaka kod zaokruživanja decimalnih brojeva.
