import sys


def montar_vetor(qtd):
    vetor = []
    for i in range(qtd):
        tempo = sys.argv[1] 
        nome = sys.argv[2]
        vetor[i] = tempo + nome
    print(vetor)
    

tempo = sys.argv[1]
qtd = int(sys.argv[1])
montar_vetor(qtd)
