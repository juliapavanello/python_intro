import sys

valor = int(sys.argv[1])
lista = []

for n in sys.argv[2:]:
    lista.append(int(n)) # fateamento de strings

def busca(vetor, v):
    for i in range(len(vetor)):
        if(vetor[i] == v):
            return i
    return -1

index = busca(lista, valor)

if index == -1:
    print ('Valor não encontrado')
else:
    print (f'Valor encontrado no indice {index}')


print (lista)