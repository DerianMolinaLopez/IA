from Node import Node

class Anchura:
    def __init__(self, raiz):
        self.raiz = raiz
        self.meta = None#de momento sera None mas adelante se le da un valor

    def BFS(self, fila, meta):  # LA FILA ES UN ARRAY!!!
        self.meta = meta  # asigno mi meta para mi metodo externo
        if not fila:  # si esta vacia se detiene
            print("No se pudo encontrar el estado meta")
            return
        else:
            nodo_actual = fila.pop(0)
            print("Explorando nodo:", nodo_actual.value)

            if self.goalTest(nodo_actual.value):
                print("Meta encontrada:", nodo_actual.value)
                return

            hijos = self.expand(nodo_actual)#exploramos los siguientes hijos a lo ancho
            fila.extend(hijos)

            self.BFS(fila, meta)

    def expand(self, nodo):#para los hijos de un nodo, extraigo todos sus hijos y los retorno
        return nodo.get_children()

    def goalTest(self, valor):#verifico si mi estado actual valor, es mi estado de aceptacion en este cado estado meta
        return valor == self.meta

#si pueden optimizar este apartado estaria bien, por que la forma de agregar los nodos si esat larga si asignas varios hijos
nodo_raiz = Node(1)
nodo_raiz.add_child(Node(2))
nodo_raiz.add_child(Node(3))
nodo_raiz.children[0].add_child(Node(4))
nodo_raiz.children[0].add_child(Node(5))
nodo_raiz.children[1].add_child(Node(6))
nodo_raiz.children[1].add_child(Node(7))


arbol = Anchura(nodo_raiz)#nodo raiz que sera mi estado inicial


fila_inicial = [nodo_raiz]  #ocupo que sea un array por la exploracion que hace

arbol.BFS(fila_inicial, 5)
print(nodo_raiz.__str__())
