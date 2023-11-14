import requests
import pandas as pd

# Definición de la clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adyacentes = []
        self.adyacentesCosto = dict()

    def agregar_adyacente(self, nodo, costo):
        self.adyacentes.append(nodo)
        self.adyacentesCosto.update({nodo: costo})

    def obtener_adyacentes(self):
        return self.adyacentes

    def getNombre(self):
        return self.nombre

    def getCosto(self, nombre):
        return self.adyacentesCosto.get(nombre)

# Función para calcular la distancia entre ciudades (puede que necesites una clave API)
import requests
import pandas as pd

def calcular_distancia(ciudad_origen, ciudad_destino, api_key="AIzaSyD6Sg3csJVzgI6RxNS_m1NsZxdblPzshWY"):
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": ciudad_origen,
        "destinations": ciudad_destino,
        "key": api_key
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    try:
        # Intenta obtener la distancia si está presente en la respuesta
        distancia = data["rows"][0]["elements"][0]["distance"]["text"]
        r = distancia.replace(" km", "").replace(" m", "").replace(",", "")
        return int(r)
    except KeyError:
        # Si 'distance' no está presente, imprime un mensaje y devuelve None
        print("La respuesta de la API no contiene la información esperada.")
        return None


# Nodos
Kiev = Nodo('Kiev, Ucrania')
Sofia = Nodo('Sofia, Bulgaria')
Atenas = Nodo('Atenas, Grecia')
Viena = Nodo('Viena, Austria')
Lisboa = Nodo('Lisboa, Portugal')
Bucarest = Nodo('Bucarest, Romania')
Berlín = Nodo('Berlín, Germany')
Zagreb = Nodo('Zagreb, Croatia')
Ámsterdam = Nodo('Ámsterdam, Netherlands')
Bruselas = Nodo('Bruselas, Belgium')
Berna = Nodo('Berna, Francia')
Andorra = Nodo('Andorra la Vella, Andorra')

# Lista de Adyacentes
#arad.agregar_adyacente(sibiu, 140) <--(ciudad,costo int)
Kiev.agregar_adyacente(Berlín, calcular_distancia(Kiev.getNombre(),Berlín.getNombre()))
Kiev.agregar_adyacente(Bucarest, calcular_distancia(Kiev.getNombre(),Bucarest.getNombre()))

Sofia.agregar_adyacente(Bucarest,calcular_distancia(Sofia.getNombre(),Bucarest.getNombre()))
Sofia.agregar_adyacente(Zagreb,calcular_distancia(Sofia.getNombre(),Zagreb.getNombre()))

Atenas.agregar_adyacente(Zagreb,calcular_distancia(Atenas.getNombre(),Zagreb.getNombre()))

Viena.agregar_adyacente(Zagreb,calcular_distancia(Viena.getNombre(),Zagreb.getNombre()))
Viena.agregar_adyacente(Berna,calcular_distancia(Viena.getNombre(),Berna.getNombre()))

Lisboa.agregar_adyacente(Andorra,calcular_distancia(Lisboa.getNombre(),Andorra.getNombre()))

Bucarest.agregar_adyacente(Kiev,calcular_distancia(Bucarest.getNombre(),Kiev.getNombre()))
Bucarest.agregar_adyacente(Sofia,calcular_distancia(Bucarest.getNombre(),Sofia.getNombre()))
Bucarest.agregar_adyacente(Zagreb,calcular_distancia(Bucarest.getNombre(),Zagreb.getNombre()))

Berlín.agregar_adyacente(Ámsterdam,calcular_distancia(Berlín.getNombre(),Ámsterdam.getNombre()))
Berlín.agregar_adyacente(Bruselas,calcular_distancia(Berlín.getNombre(),Bruselas.getNombre()))
Berlín.agregar_adyacente(Kiev,calcular_distancia(Berlín.getNombre(),Kiev.getNombre()))

Zagreb.agregar_adyacente(Bucarest,calcular_distancia(Zagreb.getNombre(),Bucarest.getNombre()))
Zagreb.agregar_adyacente(Sofia,calcular_distancia(Zagreb.getNombre(),Sofia.getNombre()))
Zagreb.agregar_adyacente(Atenas,calcular_distancia(Zagreb.getNombre(),Atenas.getNombre()))
Zagreb.agregar_adyacente(Viena,calcular_distancia(Zagreb.getNombre(),Viena.getNombre()))

Ámsterdam.agregar_adyacente(Berlín,calcular_distancia(Ámsterdam.getNombre(),Berlín.getNombre()))
Ámsterdam.agregar_adyacente(Bruselas,calcular_distancia(Ámsterdam.getNombre(),Bruselas.getNombre()))

Bruselas.agregar_adyacente(Ámsterdam,calcular_distancia(Bruselas.getNombre(),Ámsterdam.getNombre()))
Bruselas.agregar_adyacente(Berlín,calcular_distancia(Bruselas.getNombre(),Berlín.getNombre()))
Bruselas.agregar_adyacente(Berna,calcular_distancia(Bruselas.getNombre(),Berna.getNombre()))

Berna.agregar_adyacente(Bruselas,calcular_distancia(Berna.getNombre(),Bruselas.getNombre()))
Berna.agregar_adyacente(Viena,calcular_distancia(Berna.getNombre(),Viena.getNombre()))
Berna.agregar_adyacente(Andorra,calcular_distancia(Berna.getNombre(),Andorra.getNombre()))

Andorra.agregar_adyacente(Lisboa,calcular_distancia(Andorra.getNombre(),Lisboa.getNombre()))
Andorra.agregar_adyacente(Berna,calcular_distancia(Andorra.getNombre(),Berna.getNombre()))


# Lista de Ciudades
ciudades = [Kiev, Sofia, Atenas, Viena, Lisboa, Bucarest, Berlín, Zagreb, Ámsterdam, Bruselas, Berna, Andorra]

# Algoritmo A*
def algoritmo_a_estrella(inicio, objetivo):
    frontera = [(0, inicio, 0)]  # (total, nodo, gn)
    lista_ya_visitados = []

    while frontera:
        valor = frontera.pop(0)

        if valor[1].getNombre() == objetivo.getNombre():
            return valor[0]

        if valor[1].getNombre() in lista_ya_visitados:
            continue

        estado_actual = valor[1]
        lista_ya_visitados.append(estado_actual.getNombre())

        sucesores = estado_actual.obtener_adyacentes()
        sucesores = evaluacion(valor[2], sucesores, estado_actual)
        frontera += sucesores
        frontera.sort()

    return None

def evaluacion(acumulado, sucesores, anterior):
    lista_temp = []
    for sucesor in sucesores:
        gn = acumulado + anterior.getCosto(sucesor)
        lista_temp.append((gn, sucesor, gn))

    return lista_temp

# Generar tabla de costos
tabla_costos = []
for i in range(len(ciudades)):
    fila = [ciudades[i].getNombre()]
    for j in range(len(ciudades)):
        if i == j:
            fila.append(0)
        else:
            costo = algoritmo_a_estrella(ciudades[i], ciudades[j])
            fila.append(costo)
    tabla_costos.append(fila)

# Crear DataFrame
df = pd.DataFrame(tabla_costos, columns=["Ciudad"] + [ciudad.getNombre() for ciudad in ciudades])
print(df)

# Guardar DataFrame en un archivo CSV
df.to_csv("tabla_costos.csv", index=False)

