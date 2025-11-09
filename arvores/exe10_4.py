class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def contar_nodos(raiz):
    if raiz is None:
        return 0
    else:
        return 1 + contar_nodos(raiz.left) + contar_nodos(raiz.right)
