from collections import deque

n = int(input())
filas = {}  

for _ in range(n):
    nome = input().strip()
    tam = len(nome)
    if tam not in filas:
        filas[tam] = deque()
    filas[tam].append(nome)

while any(filas.values()):
    linha = []
    for tam in sorted(filas.keys()):
         if filas[tam]:
            linha.append(filas[tam].popleft())
    print(" ".join(linha))
    
