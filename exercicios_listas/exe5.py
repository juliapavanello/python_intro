class Node:
    def __init__(self, element, next):
      self.element = element
      self.next = next

class LinkedList:
   def __init__(self):
      self.size = 0
    
   def __len__(self):
      return 0
   
   def __insert_between__(self, e, predecessor, succesor):
      new = Node(e, p)