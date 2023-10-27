import matplotlib.pyplot as plt
from diccionarioGrafico import puntos, lines
import tkinter as tk
from tkinter import ttk


class MapaCiudades:
    def __init__(self, puntos, lines):
        self.puntos = puntos
        self.lines = lines

    def dibujar_ciudades(self):
        for punto, coordenadas in self.puntos.items():
            plt.plot(coordenadas[0], coordenadas[1], marker='o', markersize=8, color='blue')
            plt.text(coordenadas[0], coordenadas[1], punto, fontsize=12, ha='right')

    def dibujar_lineas(self):
        for (city1, city2), distance in self.lines.items():
            plt.plot([self.puntos[city1][0], self.puntos[city2][0]], [self.puntos[city1][1], self.puntos[city2][1]],
                     color='red', linestyle='-', linewidth=2)
            plt.text((self.puntos[city1][0] + self.puntos[city2][0]) / 2,
                     (self.puntos[city1][1] + self.puntos[city2][1]) / 2, str(distance), fontsize=10, color='green')

    def resaltar_ruta(self, ciudades_a_resaltar):
        for i in range(len(ciudades_a_resaltar) - 1):
            city1, city2 = ciudades_a_resaltar[i], ciudades_a_resaltar[i + 1]
            if (city1, city2) in self.lines:
                distance = self.lines[(city1, city2)]
                # Dibujar la línea resaltada
                plt.plot([self.puntos[city1][0], self.puntos[city2][0]], [self.puntos[city1][1], self.puntos[city2][1]],
                         color='blue', linestyle='-', linewidth=4)
                # Etiqueta de distancia

            elif (city2, city1) in self.lines:  # Intenta la tupla en el orden inverso
                distance = self.lines[(city2, city1)]
                # Dibujar la línea resaltada
                plt.plot([self.puntos[city1][0], self.puntos[city2][0]], [self.puntos[city1][1], self.puntos[city2][1]],
                         color='blue', linestyle='-', linewidth=4)
                # Etiqueta de distancia

            else:
                print(f"No se encontró la distancia entre {city1} y {city2}")
                continue

        # Esto es para el zoom de la imagen
        plt.xlim(0, 10)
        plt.ylim(-7, 10)

        # Ocultamos los ejes
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.axis('off')
        plt.show()


# Coordenadas de ciudades y líneas entre ellas
# (tu código para definir puntos y lines aquí)

# Lista de ciudades a resaltar en el orden dado

'''ciudades_a_resaltar = ['Dobreta', 'Craiova', 'Mehadia', 'Pitesti', 'Bucarest']
# Crear una instancia de la clase MapaCiudades y dibujar las ciudades y las rutas
mapa = MapaCiudades(puntos, lines)
mapa.dibujar_ciudades()
mapa.dibujar_lineas()
mapa.resaltar_ruta(ciudades_a_resaltar)

'''

