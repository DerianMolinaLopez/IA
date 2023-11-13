from itertools import permutations

elementos = [1, 2, 3]

# Obtener permutaciones de longitud 2
permutaciones = permutations(elementos, 2)

# Imprimir las permutaciones
for perm in permutaciones:
    print(perm)
