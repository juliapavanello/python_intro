class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def contar_nodes_left(raiz):
    if raiz is None:
        return 0
    contador = 0
    if raiz.left is not None:
        if raiz.left.left is None and raiz.left.right is None:
          contador += 1
        contador = contador + contar_nodes_left(raiz.left)
    if raiz.right is not None:
        contador = contador + contar_nodes_left(raiz.right)
    return contador

raiz = Node(3)
raiz.left = Node(9)    # Folha left (Conta +1)
raiz.right = Node(20)

raiz.left.left = Node(1) # Folha left (Conta +1)
# 9 não tem filho direito
raiz.left.right = None 

raiz.right.left = Node(15) # Folha left (Conta +1)
raiz.right.right = Node(7)   # Folha right (Não conta)

resultado = contar_nodes_left(raiz)
print(f"O número de folhas que são filhas esquerdas é: {resultado}")