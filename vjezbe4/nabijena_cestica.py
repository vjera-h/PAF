#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. 
# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom 
# magnetnom polju B = (0, 0, B) i ima sve tri komponente početne brzine različite od 0. 
# Kako se u tom slučaju giba elektron, a kako pozitron?
# Prikažite grafove gibanja elektrona i pozitrona za nekoliko kombinacija vrijednosti 
# električnog i magnetskog polja.

import numpy as np
import matplotlib.pyplot as plt

def lorentz(stanje, q, m, E, B):
    #stanje = [x, y, z, vx, vy, vz] vektor stanja sustava u određenom trenutku
    #opisuje ga 6 brojeva jer smo u 3D prostoru
    v = stanje[3:] #m/s obuhvaća zadnja 3 elementa - vx, vy, vz

    #lorentzova sila F = q(E + v x B)
    F = q * (E + np.cross(v, B)) #np.cross() vraca vektorski produkt dva array vektora
    #F = am, a = F/m
    a = F/m

    return np.concatenate((v, a)) #vraca kombiniran array

def rk4_korak(stanje, q, m, E, B, dt):
    k1 = lorentz(stanje, q, m, E, B)
    k2 = lorentz(stanje + k1 * dt/2, q, m, E, B)
    k3 = lorentz(stanje + k2 * dt/2, q, m, E, B)
    k4 = lorentz(stanje + k3 * dt, q, m, E, B)

    novo_stanje = stanje + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    return novo_stanje

# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom 
# magnetnom polju B = (0, 0, B) i ima sve tri komponente početne brzine različite od 0.

dt = 0.01
korak = 2000

B = np.array([0, 0, 2]) #magnetno polje u z smjeru
E = np.array([0.2, 0, 0]) #električno polje u x smjeru

v0 = np.array([0.2, 0.1, 0.6]) #početna brzina sa svim komponentima različitim od 0
r0 = np.array([0, 0, 0]) #početni položaj

def graf_gibanja(korak, dt, B, E, v0, r0):
    stanje_e = np.concatenate((r0, v0)) #vraca kombinirani array stanje = [x, y, z, vx, vy, vz]
    stanje_p = np.concatenate((r0, v0))

    elektron = []
    pozitron = []

    for k in range(0, korak): #petlja se ponavlja za svaki korak
        elektron.append(stanje_e[:3].copy()) #copy() se koristi za spremanje trenutnih vrijednosti
        pozitron.append(stanje_p[:3].copy())

        stanje_e = rk4_korak(stanje_e, -1, 1, E, B, dt) #sljedece vrijednosti
        stanje_p = rk4_korak(stanje_p, 1, 1, E, B, dt)

    elektron_array = np.array(elektron) #kako bi sve s cime radimo plot bia array   
    pozitron_array = np.array(pozitron)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(elektron_array[:, 0], elektron_array[:, 1], elektron_array[:, 2], label = 'Elektron')
    ax.plot3D(pozitron_array[:, 0], pozitron_array[:, 1], pozitron_array[:, 2], label = 'Pozitron')
    ax.set_title('Gibanje cestice')
    ax.legend()
    plt.show()

graf_gibanja(korak, dt, B, E, v0, r0) 

# Prikažite grafove gibanja elektrona i pozitrona za nekoliko kombinacija vrijednosti 
# električnog i magnetskog polja.

B1 = np.array([0, 4, 0]) #magnetno polje u z smjeru
E_0 = np.array([0, 0, 0]) #ako ne djeluje elektricna sila

graf_gibanja(korak, dt, B1, E_0, v0, r0) 

B2 = np.array([1, 0, 0]) #magnetno polje u z smjeru
E2 = np.array([0, 0, 2]) #ako ne djeluje elektricna sila

graf_gibanja(korak, dt, B2, E2, v0, r0) 