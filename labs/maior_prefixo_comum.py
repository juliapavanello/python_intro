vetor = ["olai","olaisver","olaisveira"]
aux = ""
pref = ""
count = -1

for i in range(len(vetor[0])):
    count = count+1
    aux = vetor[1][count]
    pref += aux
    for j in range(len(vetor)):
        if(aux != vetor[j][count]):
            break

print(pref)

vetor = ["olai","olaisver","olaisveira"]
pref = ""
count = -1

for i in range(len(vetor[0])):
    count += 1
    aux = vetor[0][count]  # pega letra da primeira palavra como referência
    todos_iguais = True

    for j in range(1, len(vetor)):
        if count >= len(vetor[j]) or aux != vetor[j][count]:
            todos_iguais = False
            break

    if not todos_iguais:
        break  # sai do laço externo se encontrar diferença

    pref += aux

print(pref)
