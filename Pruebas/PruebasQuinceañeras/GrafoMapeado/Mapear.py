import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from diccionariosLineasPuntos import puntos, lineas

class Mapeado:
    def __init__(self):
        self.puntos = puntos
        self.lineas = lineas

    def graficar_puntos(self):
        # Cargar la imagen de fondo
        background_img = mpimg.imread('IA/Pruebas/PruebasQuinceañeras/GrafoMapeado/Mapa.jpg')

        # Crear el gráfico
        plt.figure(figsize=(10, 8))
        plt.imshow(background_img, extent=[-50, 50, -50, 50])

        for punto, coordenadas in self.puntos.items():
            plt.plot(coordenadas[0], coordenadas[1], marker='o', markersize=8, color='blue')
            plt.text(coordenadas[0], coordenadas[1], punto, fontsize=12, ha='right')

        # Graficar las líneas
        self.graficar_lineas()

        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Grafo')
        plt.grid(False)
        plt.axis('off')
        plt.show()

    def graficar_lineas(self):
        for (ciudad1, ciudad2), propiedades in self.lineas.items():
            coords_ciudad1 = self.puntos[ciudad1]
            coords_ciudad2 = self.puntos[ciudad2]
            plt.plot([coords_ciudad1[0], coords_ciudad2[0]],
                     [coords_ciudad1[1], coords_ciudad2[1]],
                     linestyle=propiedades['linestyle'],color='blue', linewidth=2)

# Uso de la clase y graficación de puntos con imagen de fondo
objeto = Mapeado()
objeto.graficar_puntos()
