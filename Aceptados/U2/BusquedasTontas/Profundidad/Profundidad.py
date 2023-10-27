# Definición de una clase TreeNode para crear nodos de un árbol

class TreeNode:
    def __init__(self,  value):
        self.value = value
        self.children = []

    def Has_children(self):
        # Comprueba si un nodo tiene hijos
        return len(self.children) > 0

    def get_children(self, value):
        # Obtiene los hijos de un nodo con un valor específico
        if self.value == value:
            return [child.value for child in self.children]

        for child in self.children:
            result = child.get_children(value)
            if result:
                return result
        return []


# Creación de nodos y establecimiento de relaciones padre-hijo para construir un árbol
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node14 = TreeNode(14)
node15 = TreeNode(15)
node16 = TreeNode(16)
node17 = TreeNode(17)
node18 = TreeNode(18)

# Establecimiento de relaciones padre-hijo entre los nodos
node1.children = [node2, node3]
node2.children = [node5, node6]
node3.children = [node7, node8]
node5.children = [node9, node10]
node6.children = [node11, node12]
node7.children = [node14]
node8.children = [node15, node16]
node12.children = [node17]
node14.children = [node18]


# Función para imprimir el árbol de manera recursiva
def print_tree(node, indent=0):
    print(" " * indent + str(node.value))
    for child in node.children:
        print_tree(child, indent + 2)


# Imprimir el árbol
print_tree(node1)

# Inicialización de variables para realizar una búsqueda en profundidad (DFS)
F = [1]  # Lista de nodos a explorar
# A = []  # Lista para almacenar nodos visitados
M = 17  # Valor objetivo que se busca en el árbol


# Función GoalTest para verificar si un nodo es igual al valor objetivo
def GoalTest(A):
    return A == M


# Función Expand para obtener los hijos de un nodo
def Expand(A):
    raíz = node1
    return raíz.get_children(A)




def DFSC(f):
    if len(f) == 0:
        print("Lista vacía")
    else:
        A = f.pop(0)  # Obtener el primer nodo de la lista
        if GoalTest(A):
            print('Se encontró el valor objetivo')
        else:
            hijos = Expand(A)
            S = f.copy()
            hijos.extend(S)
            f = hijos
            print(f)  # Imprimir la lista de nodos a explorar
            DFSC(f)


DFSC(F)