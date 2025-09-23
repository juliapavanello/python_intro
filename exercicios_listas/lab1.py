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
pref = ""
#n log n
vetor_ordenado = sorted(vetor)

for i in range(len(vetor_ordenado[0])):
    if vetor_ordenado[0][i] == vetor_ordenado[len(vetor_ordenado)-1][i]:
        pref += vetor_ordenado[0][i]
    else:
        break

print(pref)