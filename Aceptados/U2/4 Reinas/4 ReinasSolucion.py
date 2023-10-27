
from tablero import TableroAjedrez
solucion = []
def ataques(v):
    n = len(v)
    total_ataques = 0

    for i in range(n):
        for j in range(i + 1, n):
            if v[i] == v[j] or abs(i - j) == abs(v[i] - v[j]):
                total_ataques += 2

    return total_ataques


def imprimir_tablero(v):
    n = len(v)
    for i in range(n):
        fila = ["0" for _ in range(n)]
        fila[v[i]] = "1"
        print(" ".join(fila))


# nuevo
def Reacomodo_lista(a):
    RESULTADOS = []
    Recorer = []

    for elemento in a:
        if isinstance(elemento, list) and Recorer:
            RESULTADOS.append(Recorer)
            Recorer = []
        Recorer.append(elemento)

    if Recorer:
        RESULTADOS.append(Recorer)

    return RESULTADOS


def Evaluate(a):
    OPCION = []
    for sublista in a:
        OPCION.append(sublista)
        OPCION.append(ataques(sublista))
        # print(OPCION)
    OPCION = Reacomodo_lista(OPCION)
    # print(OPCION)
    return OPCION


def Sort(a):
    # Definimos una función de ordenamiento personalizada
    # print(a)
    def clave_ordenamiento(sublista):
        # La clave de ordenamiento es el segundo elemento de la sublista
        return sublista[1]

    # Utilizamos la función sorted con la clave de ordenamiento
    sort = sorted(a, key=clave_ordenamiento)
    # print(sort)
    return sort


def GoalTest(a):
    return ataques(a) == 0


def expand(a):
    N = len(a)
    resultados = []
    for i in range(N):
        copia = a.copy()
        if (copia[i] < N):
            copia[i] = copia[i] + 1
        resultados.append(copia)
    # print(resultados)
    return resultados


# Lista_visitada=[]

def GS(F):
    global solucion  # Utilizar la variable global solucion

    if len(F) == 0:
        print("Lista vacía")
    else:
        A = F
        print("------------------")
        print("F ACTUAL")
        print(A)

        if GoalTest(A):
            print("Solucion Encontrada")
            solucion = A  # Asignar la solución encontrada a la variable global
            print(A)
        else:
            Os = expand(A)
            print("EXPAN")
            print(Os)
            Op = Evaluate(Os)
            Os = Sort(Op)
            print("LISTA")
            print(Os)

            if F == Os[0][0]:
                print("son iguales")
                print(Os[3][0])
                GS(Os[3][0])
            else:
                print("LA MEJOR OPCIONE")
                print(Os[0][0])
                GS(Os[0][0])


'''
cuando busca la segunda reina mas optima, deberia irse a 4, no a 5
'''
# expand([1, 1, 1, 1])
F = [1]*4  # asi debe mandar los datos en expand
# F = [2, 4, 1, 1]
# print(expand(F))
# F = [[1, 1, 1, 1]]
# print(F[1])

GS(F)
tablero_ajedrez = TableroAjedrez()
tablero_ajedrez.asignar_dimension(solucion)
tablero_ajedrez.dibujar_tablero()
# A=[[2, 4, 1, 1]]
# E = expand(F)
# print(E)

