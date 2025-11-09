import heapq

m, n = map(int, input().split())
fila = []
for i in range(n):
    hora, nome = input().split()
    h, min = map(int, hora.split(":"))
    minutos = h * 60 + min
    if h < 12:
        minutos += 24 * 60
    heapq.heappush(fila, (minutos, i, nome))

res = []
for minutos, i, nome in fila:
    dif = abs(minutos - (24 * 60))
    if dif <= m:
        res.append((minutos, i, nome))

for _, _, nome in sorted(res):
    print(nome)
