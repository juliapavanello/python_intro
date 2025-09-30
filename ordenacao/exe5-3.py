def bubble_sort(array):
    # Repete até organizar toda a lista
    for i in range(len(array)):
        # Compara cada par de elementos vizinhos
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                # Troca se estiver fora de ordem
                array[j], array[j + 1] = array[j + 1], array[j]


array = [10, 9, 11, 23, 7, 33, 45,2]
print(bubble_sort(array))

