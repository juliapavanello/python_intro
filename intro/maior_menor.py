import sys
maior = float('-inf')
menor = float('inf')
lista = []

for n in sys.argv[2:]:
    lista.append(int(n)) # fateamento de strings
    

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    
    if lista[i] < menor:
        menor = lista[i]

    if lista[i] < 0:
        lista[i] = 0

print(f'Menor: {menor} e maior: {maior}')
print(lista)