import random
import math

class DemoCombination():
    def __init__(self, collection):
        self.collection = collection
        self.combinations = []

    def calculateCombinationsCount(self, k):
         #calculamos todas las coombinaciones de k elementos, en este caso, serian si o si 7
        combinations_count = math.comb(len(self.collection), k)
        return combinations_count

    def makeCombinations(self, element):
        if element in self.collection:
            '''
            Necesitamos eliminar el elemento que ingresemos al algoritmo
            para no tener problema al hacer combinaciones
            '''
            temp_collection = self.collection.copy()
            temp_collection.remove(element)
            combinations_count = self.calculateCombinationsCount(7)  # Calcular combinaciones de 7 elementos
            for _ in range(combinations_count):#usamos una variable anonima ya que no necesito el puntero
                combination = random.sample(temp_collection, 7)
                self.combinations.append(combination)
            return self.combinations
        else:
            return None

combinaciones = DemoCombination([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Número de combinaciones posibles:", combinaciones.calculateCombinationsCount(7))
#print("Combinaciones generadas (excluyendo el elemento 1):")
print(len(combinaciones.makeCombinations(1)))
#print(combinaciones.makeCombinations(1))

