
x1 = float(input('unesite koordinatu x prve tocke: '))
y1 = float(input('unesite koordinatu y prve tocke: '))
x2 = float(input('unesite koordinatu x druge tocke: '))
y2 = float(input('unesite koordinatu y druge tocke: '))
print('prva ({}, {}) i druga ({}, {}) tocka'.format(x1, y1, x2, y2))
z = (y2-y1)/(x2-x1)
l = y1 - z * x1
print('jednadzba pravca: y = {}x + {}'.format(z,l))