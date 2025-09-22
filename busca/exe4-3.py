# Busca binária em um vetor, retorna a posição

def busca_binaria(vetor, valor):
    low = 0
    high = len(vetor) - 1

    while low <= high:
        mid = (high + low)//2 # para pegar o valor inteiro usa-se //
        if vetor[mid] == valor:
            return mid
        if vetor[mid] < valor:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def busca_sequencial(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
        if vetor[i] < valor:
            return -1
    return -1


vetor = [1, 2, 4, 7, 11, 17, 21]
print(busca_binaria(vetor, 21))
print(busca_sequencial(vetor, 21))