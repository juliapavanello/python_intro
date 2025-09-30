from node import Node
from node import Node2

class LinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def size2(self):
        count = 0
        walk = self.head.next          
        while walk is not self.tail:  
            count += 1
            walk = walk.next
        return count
    
    def is_empty(self):
        return self.size != 0
    
    def inserir_inicio(self, e):
        new = Node2(self, e)
        new.next = self.head
        self.head = new
        if self.tail is None:
            self.tail = new
        self.size += 1

    def inserir_final(self, e):
        new = Node2(self, e)
        if self.is_empty:
            self.head = new
            self.tail = new
        else:
            self.tail.next = e
            self.tail = e
        self.size += 1
    
    def remove_inicio(self):
        if self.is_empty():
            raise IndexError("A lista está vazia")
        self.head = self.head.next 
        if self.head is None:            # se removeu o último elemento
            self.tail = None
        self._size -= 1

    def remove_final(self):
        if self.is_empty():
            raise IndexError("A lista está vazia")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            walk = self.head
            while walk.next != self.tail:
                walk = walk.next
            walk.next = None
            self.tail = walk
        self._size -= 1

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
    
    def clear(self):
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

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
    
    def size(self):
        count = 0
        walk = self.header.next          
        while walk is not self.trailer:  
            count += 1
            walk = walk.next
        return count
    
    def central(self):
        walk1 = self.header.next     
        walk2 = self.trailer.prev     
        while walk1 != walk2 and walk1.next != walk2: 
            walk1 = walk1.next
            walk2 = walk2.prev
        return walk1
