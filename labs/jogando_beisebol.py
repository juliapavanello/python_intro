def jogo_de_beisebol(operacoes):
    pilha = []

    for op in operacoes:
        if op == "C":
            pilha.pop()
        elif op == "D":
            pilha.append(pilha[-1] * 2)
        elif op == "+":
            pilha.append(pilha[-1] + pilha[-2])
        else:
            pilha.append(int(op))

    return sum(pilha)


# Exemplos de teste:
print(jogo_de_beisebol(["5", "2", "C", "D", "+"]))          # saida 30
print(jogo_de_beisebol(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # saida 27
print(jogo_de_beisebol(["1", "C"]))                         # saida 0
