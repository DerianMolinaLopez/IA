import requests
import pandas as pd

def calcular_distancia(ciudad_origen, ciudad_destino, api_key):
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": ciudad_origen,
        "destinations": ciudad_destino,
        "key": api_key
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    distancia = data["rows"][0]["elements"][0]["distance"]["text"]


    return distancia


distancia =0

print(f"Distancia: {distancia}")
################################################################################################
#realzo mi arreglo
CiudadesEuropeas = [
    ['Kiev, Ucrania'],
    ['Sofia, Bulgaria'],#sofia
    ['Atenas, Grecia'],
    ['Viena, Austria'],
    ['Lisboa, Portugal'],#lisboa
    ['Bucarest, Rumanía'],
    ['Berlín, Alemania'],
    ['Zagreb, Croacia'],
    ['Ámsterdam, Países Bajos'],
    ['Bruselas, Bélgica'],
    ['Berna, Suiza'],
    ['Andorra la Vella, Andorra']
]
#####################################################
#print(CiudadesEuropeas[1][0])


'''
realizamos un for anidado para sacar las distancias entre cada una de las ciudades
uno anidado de momento ya que es una solucion lenta que consume solicitudes a la api
'''
api_key ="AIzaSyD6Sg3csJVzgI6RxNS_m1NsZxdblPzshWY"

for i in range(0, len(CiudadesEuropeas)):
    ciudad_origen = CiudadesEuropeas[i][0]
    print(f"{ciudad_origen}******************************************")
    for j in range(0, len(CiudadesEuropeas)):
        ciudad_destino = CiudadesEuropeas[j][0]

        distancia = calcular_distancia(ciudad_origen, ciudad_destino, api_key)
        print(f"origen{ciudad_origen}\n{ciudad_destino}\n{distancia}")
        CiudadesEuropeas[i].append(
            calcular_distancia(ciudad_origen, ciudad_destino, api_key)
        )
#chechamos las salidas
#print(CiudadesEuropeas)
df = pd.DataFrame(CiudadesEuropeas, columns=["Ciudad", "Kiev, Ucrania", "Sofia, Bulgaria", "Atenas, Grecia", "Viena, Austria","Lisboa, Portugal", "Bucarest, Rumanía", "Berlín, Alemania", "Zagreb, Croacia", "Ámsterdam, Países Bajos", "Bruselas, Bélgica", "Berna, Suiza", "Andorra la Vella, Andorra" ]) # Asigna nombres a las columnas y al índice
df.to_csv("lista.csv", index=False) # Guarda el DataFrame en un archivo csv sin el índice






