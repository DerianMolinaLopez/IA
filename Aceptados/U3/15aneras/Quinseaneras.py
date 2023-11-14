from IPython.display import display
import gmaps
import googlemaps
from ipywidgets import interactive
from IPython.display import display
from ipywidgets.embed import embed_minimal_html

from ProyectoU2P2.CiudadesObj import Ciudad
import math
import pandas as pd
from itertools import permutations
from gmplot import gmplot
gx = pd.read_csv("tabla_costos.csv")
gx = gx.set_index('Ciudad')
def getDistanciaAS(ori, fin):
    r =gx.loc[ori,fin]

    return r

def distancia(X1,Y1,X2,Y2):
  return abs(math.sqrt(((X2 - X1)**2) + ((Y2 - Y1)**2)))

def permutList(l):
  if not l:
    return [[]]
  l.append(l[0])
  subciudades = l[1:8]
  return list(permutations(subciudades))

Kiev = Ciudad("Kiev, Ucrania",    50.467981379817815, 30.527779407460397)
Sofia = Ciudad("Sofia, Bulgaria",    42.69985582624216, 23.31775344745848)
Atenas = Ciudad("Atenas, Grecia",    37.972675434696434, 23.719077070526172)
Viena = Ciudad("Viena, Austria",    48.206825617973095, 16.37674883580833)
Lisboa = Ciudad("Lisboa, Portugal",    38.72235565217588, -9.132939181769217)
Bucarest = Ciudad("Bucarest, Romania",    44.426763958980914, 26.105621291454796)
Berlín = Ciudad("Berlín, Germany",    52.519683845446124, 13.393824044940256)
Zagreb = Ciudad("Zagreb, Croatia",    45.815233909185984, 15.984274198017319)
Ámsterdam = Ciudad("msterdam, Netherlands",    52.36922271743421, 4.900299838856)
Bruselas = Ciudad("Bruselas, Belgium",    50.84763858612332, 4.352281687217245)
Berna = Ciudad("Berna, Francia",    49.089525613424904, 0.5961545304840539)
Andorra = Ciudad("Andorra la Vella, Andorra",    42.50643748395003, 1.5219176066786817)


Lisboa.setVecinos([Andorra])
Andorra.setVecinos([Lisboa, Berna])
Berna.setVecinos([Andorra, Bruselas, Viena])
Bruselas.setVecinos([Ámsterdam, Berlín, Berna])
Ámsterdam.setVecinos([Berlín, Bruselas])
Berlín.setVecinos([Ámsterdam, Bruselas, Kiev])
Kiev.setVecinos([Berlín, Bucarest])
Bucarest.setVecinos([Sofia, Kiev, Zagreb])
Sofia.setVecinos([Zagreb, Bucarest])
Zagreb.setVecinos([Atenas, Bucarest, Sofia, Viena])
Viena.setVecinos([Berna, Zagreb])
Atenas.setVecinos([Zagreb])

ciudades = {
    1 : "Kiev, Ucrania",
    2 : "Sofia, Bulgaria",
    3 : "Atenas, Grecia",
    4 : "Viena, Austria",
    5 : "Lisboa, Portugal",
    6 : "Bucarest, Romania",
    7 : "Berlín, Germany",
    8 : "Zagreb, Croatia",
    9 : "Ámsterdam, Netherlands",
    10 : "Bruselas, Belgium",
    11 : "Berna, Francia",
    12 : "Andorra la Vella, Andorra"

}


#Metodo A*
resultado = [] #formato [fx, permutacion]
ciudadInicial = ciudades[1]
ciudadesF = [ciudadInicial, ciudades[2], ciudades[3], ciudades[4], ciudades[5], ciudades[6], ciudades[7], ciudades[9], ciudadInicial]
permutaciones =permutList(ciudadesF)
for i in range(len(permutaciones)):
    permutacionActual = list(permutaciones[i])
    permutacionActual.append(ciudadInicial)
    permutacionActual.insert(0, ciudadInicial)
    acumulado = 0
    #pares_con_segundo_valor = []

    for j in range(len(permutacionActual) - 1):
        tupla_actual = (permutacionActual[j], permutacionActual[j + 1])
        ciudadActual = permutacionActual[j]
        ciudadSiguiente = permutacionActual[j+1]
        acumulado += int(getDistanciaAS(ciudadActual, ciudadSiguiente))
        #pares_con_segundo_valor.append(tupla_actual)

    resultado.append([acumulado,permutacionActual])

    resultado.append([acumulado,permutacionActual])
#ordena para sacar el mejor costo
resultado.sort()

print("**************************************")
print("La mejor ruta es:" + str(resultado[0][1]))
print("con un coste de :" + str(resultado[0][0]))

#Para graficar
#********************************************************

# Importar la librería gmplot
import gmplot
import googlemaps

ciudades = {
"Kiev, Ucrania": (50.467981379817815, 30.527779407460397),
"Sofia, Bulgaria": (42.69985582624216, 23.31775344745848),
"Atenas, Grecia": (37.972675434696434, 23.719077070526172),
"Viena, Austria": (48.206825617973095, 16.37674883580833),
"Lisboa, Portugal": (38.72235565217588, -9.132939181769217),
"Bucarest, Romania": (44.426763958980914, 26.105621291454796),
"Berlín, Germany": (52.519683845446124, 13.393824044940256),
"Zagreb, Croatia": (45.815233909185984, 15.984274198017319),
"Ámsterdam, Netherlands": (52.36922271743421, 4.900299838856),
"Bruselas, Belgium": (50.84763858612332, 4.352281687217245),
"Berna, Francia": (49.089525613424904, 0.5961545304840539),
"Andorra la Vella, Andorra": (42.50643748395003, 1.5219176066786817)
}
solucion = resultado[0][1]

key = 'AIzaSyD6Sg3csJVzgI6RxNS_m1NsZxdblPzshWY'

gmaps = googlemaps.Client(key=key)

nombres = [ciudad for ciudad in solucion]

ruta = gmaps.directions(nombres[0], nombres[-1], waypoints=nombres[1:-1], mode='driving', language='es')[0]
latitudes = []
longitudes = []
for leg in ruta['legs']:
    for step in leg['steps']:
        start = step['start_location']
        end = step['end_location']
        latitudes.append(start['lat'])
        longitudes.append(start['lng'])
        latitudes.append(end['lat'])
        longitudes.append(end['lng'])

gmap = gmplot.GoogleMapPlotter(48.8566, 2.3522, 4, apikey=key)

gmap.plot(latitudes, longitudes, 'red', edge_width=3)
gmap.draw('mapa.html')