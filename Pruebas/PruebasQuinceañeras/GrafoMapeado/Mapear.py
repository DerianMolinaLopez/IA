import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

'''
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
'''


class Mapeado:
    def __init__(self):
        self.puntos = {
            'Kiev': (10, -6.8),
            
            'Atenas': (7, -40),
            'Viena': (-6, -14),
            'Bucarest': (10, -20.5),
            'Berlin': (-9, -4),
            'Zagreb': (-5, -20),
            'Amsterdam': (-19, -2),
            'Brucelas': (-21, -6),
            'Andorra': (0, 0),
              'Paris':(-23, -10),
                'Madrid':(-37,-30),
                 'Berna':(-17, -17)  # Ajusta las coordenadas según tu necesidad
            # Agrega más puntos si es necesario
        }

    def graficar_puntos(self):
        # Cargar la imagen de fondo
        background_img = mpimg.imread('IA/Pruebas/PruebasQuinceañeras/GrafoMapeado/Mapa.jpg')

        # Crear el gráfico
        plt.figure(figsize=(10, 8))
        plt.imshow(background_img, extent=[-50, 50, -50, 50])

        for punto, coordenadas in self.puntos.items():
            plt.plot(coordenadas[0], coordenadas[1], marker='o', markersize=8, color='blue')
            plt.text(coordenadas[0], coordenadas[1], punto, fontsize=12, ha='right')


        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Grafo')
        plt.grid(False)
        plt.axis('off')
        plt.show()

# Uso de la clase y graficación de puntos con imagen de fondo
objeto = Mapeado()
objeto.graficar_puntos()


'''
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
'''
