class Node:
    def __init__(self, element, prev, next):
      self.element = element
      self.prev = prev
      self.next = next
class LinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def __delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element

    def first(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.header.next.element

    def last(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.trailer.prev.element

    def add_first(self, e):
        self.__insert_between(e, self.header, self.header.next)

    def add_last(self, e):
        self.__insert_between(e, self.trailer.prev, self.trailer)

    def remove_first(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.__delete_node(self.header.next)

    def remove_last(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.__delete_node(self.trailer.prev)

    def __str__(self):
        # Para imprimir a lista (print)
        answer = '( '
        walk = self.header.next
        while walk != self.trailer:
            answer += f'{walk.element} '
            walk = walk.next
        answer += ')'
        return answer

    def index(self, e):
        # Busca sequencial
        if self.is_empty(): return -1
        count = -1
        walk = self.header.next
        while walk != self.trailer:
            count += 1
            if walk.element == e:
                return count
            walk = walk.next
        return -1

    def concat(self, other):
      if other.is_empty():
          return

      if self.is_empty():
          # se L está vazia, L' é simplesmente other
          self.header.next = other.header.next
          other.header.next.prev = self.header
          self.trailer = other.trailer
          self.size = other.size
      else:
          # temp1 = trailer de L
          temp1 = self.trailer.prev
          # temp2 = header de M
          temp2 = other.header

          # junta L e M
          temp1.next = temp2.next
          temp2.next.prev = temp1

          # atualiza trailer de L
          self.trailer = other.trailer

          # soma os tamanhos
          self.size += other.size

    def toArray(self):
      resposta = [None] * self.__len__()
      elemento = self.header.next
      count = -1
      while elemento != self.trailer:
        count = count+1
        resposta[count] = elemento.element
        elemento = elemento.next
      return resposta

def jogar_cartas_fora_lista(baralho):
    descartadas = []
    while len(baralho) > 1:
        descartadas.append(baralho.remove_first())
        baralho.add_last(baralho.remove_first())
    return descartadas, baralho.first()

def jogar_cartas_fora_array(baralho2):
    descartadas = []
    count = 0
    restante =0
    while len(baralho2) > 1:
      descartadas.append(baralho2[0])
      baralho2.pop(0)
      restante = baralho2.pop(0)
      baralho2.append(restante)

    return descartadas, restante


L = [1,2,3,4,5,6,7]
descartadas, restante = jogar_cartas_fora_array(L)
print(descartadas)
print(restante)


L = LinkedList()
L.add_last(1)
L.add_last(2)
L.add_last(3)
L.add_last(4)
L.add_last(5)
L.add_last(6)
L.add_last(7)

print("Antes do jogo:")
print("L =", L)

descartadas, restante = jogar_cartas_fora_lista(L)

print("Depois do jogo:")
print("Descartadas:", descartadas)   # [1, 3, 5, 7, 4, 2]
print("Restante:", restante)         # 6