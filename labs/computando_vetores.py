import random
import time

n = 10**7
a, b = 580, 788
k = 73

# vetor original por conta das mudancas feitas no cenario 1 pra nao considerar o valor menor ja considerado
vetor_original = [random.randint(0, 1000) for _ in range(n)]

# cenario 1
vetor = vetor_original.copy()
menores = []

start = time.time()
while len(menores) < k:
    menor = float('inf')
    menor_idx = -1
    for i in range(len(vetor)):
        # if vetor [i] < menor and vetor[i] not in menores: # neste caso nao consideraria repeticoes
        if vetor[i] < menor:
            menor = vetor[i]
            menor_idx = i
    vetor[menor_idx] = float('inf')
    menores.insert(0, menor)

soma = 0
for v in vetor_original: 
    if a <= v <= b:
        soma += v
end = time.time()
tempo_nao_ordenado = end - start

print(f'O k-ésimo valor menor (nao ordenado) é {menores[0]}')
print(f'A soma dos valores no intervalo é {soma}')
print(f'Tempo do cenário 1 (não ordenado): {tempo_nao_ordenado:.6f} segundos')

print('------------------')

# cenario 2
start = time.time()
vetor_ordenado = sorted(vetor_original)
k_esimo = vetor_ordenado[k-1]
soma_ordenado = 0
for v in vetor_ordenado:
    if a <= v <= b:
        soma_ordenado += v
end = time.time()
tempo_ordenado = end - start

print(f'O k-ésimo valor menor (vetor ordenado) é {k_esimo}')
print(f'A soma dos valores no intervalo (vetor ordenado) é {soma_ordenado}')
print(f'Tempo do cenário 2 (ordenado): {tempo_ordenado:.6f} segundos')
