import numpy as np
import matplotlib.pyplot as plt


class TableroAjedrez:
    def __init__(self):
        self.dimension = 0
        self.tablero = None
        self.posiciones = []
    
    def asignar_dimension(self, posiciones):
        self.dimension = len(posiciones)
        self.tablero = np.zeros((self.dimension, self.dimension))
        self.posiciones = posiciones
        self.tablero[1::2, ::2] = 1  # Filas impares y columnas pares son cuadros blancos
        self.tablero[::2, 1::2] = 1  # Filas pares y columnas impares son cuadros blancos
    
        
    def dibujar_tablero(self):
        if self.tablero is not None:
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#CCCCCC')  # Establecer el color de fondo del panel a gris claro (fuera del tablero)
            ax.set_facecolor('#DDDDDD')  # Establecer el color de fondo del tablero a un tono ligeramente más oscuro
            
            ax.imshow(self.tablero, cmap='YlGnBu', interpolation='nearest')
            
            # Dibujar puntos rojos en las posiciones especificadas
            for i, posicion in enumerate(self.posiciones):
                plt.plot(posicion, i, 'ro', markersize=10)
            
            plt.xticks([])
            plt.yticks([])
            plt.grid(None)
            plt.show()
