def busca_binaria(vetor, valor, minimo, maximo):
    if minimo > maximo:
        return -1
    else:
        mid = (minimo + maximo)//2
        if valor == vetor[mid]:
            return mid
        elif valor < vetor[mid]:
            return busca_binaria(vetor, valor, minimo, mid -1)
        else:
            return busca_binaria(vetor, valor, mid + 1, maximo)
        
vetor = [1, 3, 5, 7, 9, 11, 13]
valor = 7

indice = busca_binaria(vetor, valor, 0, len(vetor)-1)
print(f'Valor encontrado no índice: {indice}')