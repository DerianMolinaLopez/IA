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
    duracion = data["rows"][0]["elements"][0]["duration"]["text"]

    return distancia, duracion


# Ejemplo de uso
ciudad_origen = "Ciudad de México, México"
ciudad_destino = "Guadalajara, México"
api_key = "AIzaSyCDsf4qaVbLl_kT1FGxWRc6PWWx4jihlo4"

distancia, duracion = calcular_distancia(ciudad_origen, ciudad_destino, api_key)
print(f"Distancia: {distancia}")
print(f"Duración del viaje: {duracion}")
