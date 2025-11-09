votos = {}
while True:
    nome = input().strip()
    if nome == "***":
        break
    votos[nome] = votos.get(nome, 0) + 1

maior = max(votos.values())
vencedores = [n for n, v in votos.items() if v == maior]

if len(vencedores) == 1:
    print(vencedores[0])
else:
    print("Segundo turno!")
