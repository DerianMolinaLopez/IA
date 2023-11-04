import requests
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
    ['Ankara, Turquía'],
    ['Atenas, Grecia'],
    ['Viena, Austria'],
    ['Estocolmo, Suecia'],
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
print(CiudadesEuropeas)





