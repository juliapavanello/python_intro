from linkedlist import LinkedList

L = LinkedList()
M = LinkedList()

L.add_last(1)
L.add_last(2)
M.add_last(3)
M.add_last(4)

print("Antes concat:")
print("L =", L)
print("M =", M)

L.concat(M)

print("Depois concat:")
print("L =", L)  # ( 1 2 3 4 )
print("M =", M)  # ( )
