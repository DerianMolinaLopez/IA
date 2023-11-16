
ListaCiudades = []

class Ciudad:

  def __init__(self, nombre, coordenadaX, coordenadaY):
    self.nombre = nombre
    self.coordenadaX = coordenadaX
    self.coordenadaY = coordenadaY
    self.listaVecinos = []
    self.distanciaActual = 0
    self.fx = 0
    self.hx = 0
    ListaCiudades.append(self)

  def getCoordenadas(self):
    return (self.coordenadaX,self.coordenadaY)

  def setVecinos(self,vecinos):
    self.listaVecinos = vecinos