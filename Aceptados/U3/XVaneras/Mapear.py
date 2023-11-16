import matplotlib.pyplot as plt
from DiccionarioLineasPuntos import puntos, lineas

class Mapeado:
    def __init__(self):
        self.puntos = puntos
        self.lineas = lineas

    def graficar_puntos(self):
        try:
            # Cargar la imagen de fondo

            # Crear el gráfico
            plt.figure(figsize=(10, 8))

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

        except FileNotFoundError:
            print("Error: No se pudo encontrar la imagen de fondo.")

    def graficar_lineas(self):
        for (ciudad1, ciudad2), propiedades in self.lineas.items():
            coords_ciudad1 = self.puntos[ciudad1]
            coords_ciudad2 = self.puntos[ciudad2]
            plt.plot([coords_ciudad1[0], coords_ciudad2[0]],
                     [coords_ciudad1[1], coords_ciudad2[1]],
                     linestyle=propiedades['linestyle'], color='blue', linewidth=2)

# Uso de la clase y graficación de puntos con imagen de fondo
objeto = Mapeado()
objeto.graficar_puntos()
