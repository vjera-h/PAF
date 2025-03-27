import matplotlib.pyplot as plt
import numpy as np

def pravac(x1, y1, x2, y2):
    z = (y2 - y1) / (x2 - x1)
    l = y1 - z * x1
    print('Jednadžba pravca: y = {}x + {}'.format(z, l))
    x_values = [x1, x2]
    y_values = [y1, y2]
    plt.plot(x_values, y_values, label='Pravac')
    plt.scatter([x1, x2], [y1, y2], color='red', zorder=5)
    plt.text(x1, y1, f'({x1},{y1})', fontsize=12, ha='right')
    plt.text(x2, y2, f'({x2},{y2})', fontsize=12, ha='right')
    plt.title('Graf pravca i točaka')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    opcija = input('Želite li prikazati graf (da/ne)? ').strip().lower()
    if opcija == 'da':
        plt.show()
    else:
        ime = input('Unesite ime za PDF datoteku (bez ekstenzije): ').strip()
        plt.savefig('{}.pdf'.format(ime))
        print('Graf je spremljen kao {}.pdf'.format(ime))
    plt.close()

x1 = float(input('Unesite koordinatu x prve točke: '))
y1 = float(input('Unesite koordinatu y prve točke: '))
x2 = float(input('Unesite koordinatu x druge točke: '))
y2 = float(input('Unesite koordinatu y druge točke: '))

pravac(x1, y1, x2, y2)