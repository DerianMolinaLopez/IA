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

    def __str__(self):
        return self.nombre

    def toString(self):
        sucesores = ', '.join([sucesor.getNombre() for sucesor in self.adyacentes])
        return f'Estado Actual: {self.nombre}, Sucesores: {sucesores}'