#Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke.
#Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. 
#Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu 
#pravca koji prolazi kroz te dvije točke.


def je_li_float(koord):
    try:
        float(koord)
        return True
    except ValueError:
        return False

while True: #petlja koja ispisuje prve dvije koordinate
    x = input('Upisite prvu x koordinatu: ')
    y = input('Upisite prvu y koordinatu: ')
    if je_li_float(x)==True and je_li_float(y)==True:
        print('Koordinate su unesene')
        x = float(x)
        y = float(y)
        break
    else:
        print('Potrebno je upisati broj')

while True: #petlja koja ispisuje druge dvije koordinate
    x1 = input('Upisite drugu x koordinatu: ')
    y1 = input('Upisite drugu y koordinatu: ')
    if je_li_float(x1)==True and je_li_float(y1)==True:
        print('Koordinate su unesene')
        x1 = float(x1)
        y1 = float(y1)
        break
    else:
        print('Potrebno je upisati broj')

a = (y1 -y)/(x1 - x)
b = y - a*x #jednadžba pravca kroz dvije točke
print(f'Jednadzba pravca je: y = {a}x + {b}')



#Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. 
#Neka ta funkcija naekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. 
#Pozovite tu funkciju u svom programu.


def jednadžba_pravca(x, y, x1, y1):
    a = (y1 -y)/(x1 - x)
    b = y - a*x
    print(f'Jednadzba pravca je: y = {a}x + {b}')

jednadžba_pravca(5, 4, 6, 9)

#Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot 
# tako da nacrtate unesene koordinate i pravac koji prolazi kroz njih. 
# Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF. 
# Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import matplotlib.pyplot as plt

def jednadžba_i_graf_pravca(x, y, x1, y1):
    a = (y1 -y)/(x1 - x)
    b = y - a*x
    print(f'Jednadzba pravca je: y = {a}x + {b}')

    plt.plot([x, x1], [a*x + b, a*x1 + b], label = 'Pravac', color = 'green')
    plt.plot(0,0)
    plt.scatter([x, x1], [y, y1], label = 'Tocke', color = 'cyan')
    plt.axhline(0, color = 'black', lw = 0.5)
    plt.axvline(0, color = 'black', lw = 0.5)
    plt.title('Graf pravca')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    graf = input('Zelite li prikazati graf(da)? Također ga možete i spremiti: ')
    if graf.lower() == 'da':
        plt.show()
    else:
        ime = input('Unesite ime pod kojim zelite spremiti graf: ')
        plt.savefig(f'{ime}.pdf')

jednadžba_i_graf_pravca(5, -4, -6, 9)

#zakašnjenje s zadatkom zato što prvi put nije upisalo dio 5. zadatka gdje prikazuje/sprema graf