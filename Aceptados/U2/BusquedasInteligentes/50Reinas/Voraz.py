from tablero import TableroAjedrez

listaNegra = []


def Ataques(reinas):
    total = 0
    for i in range(len(reinas)):
        for j in range(i + 1, len(reinas)):
            if reinas[i] == reinas[j] or abs(reinas[i] - reinas[j]) == abs(i - j):
                total += 2
    return total


def goalTest(arreglo):
    return Ataques(arreglo) == 0


def expandir(arreglo):
    resultados = []
    for i in range(len(arreglo)):
        for j in range(len(arreglo)):
            if i != j:
                arregloAux = arreglo.copy()
                arregloAux[i] = j
                if arregloAux not in listaNegra:
                    resultados.append(arregloAux)
    return resultados


def greedySearch(frontera):
    if not frontera:
        return 'No se encontró solución'

    estadoActual = frontera.pop(0)[1]
    listaNegra.append(estadoActual)

    if goalTest(estadoActual):
        return (estadoActual)
    else:
        sucesores = expandir(estadoActual)
        sucesores = [(Ataques(sucesor), sucesor) for sucesor in sucesores]
        sucesores.sort()
        frontera.extend(sucesores)
        frontera.sort()

    return greedySearch(frontera)


frontera = []
frontera.append((0, [0] * 50))
solucion = greedySearch(frontera)
print(solucion)
tablero_ajedrez = TableroAjedrez()
tablero_ajedrez.asignar_dimension(solucion)
tablero_ajedrez.dibujar_tablero()