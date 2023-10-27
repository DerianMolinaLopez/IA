class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        result = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def get_children(self):#regresamos todos los hijos
        return self.children
