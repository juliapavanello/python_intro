import sys

# Escreva um programa que crie uma lista contendo os 20 primeiros números ímpares. Ao final, exiba a
# lista em tela. Repita o processo para os 20 primeiros números primos.

impares = [0] * 20
atual = 1
for i in range(len(impares)):
    impares[i] = atual
    atual += 2
#print(impares)

def primo(n):
    for i in range(2, n):
        if (n % i):
            return False
    return True

primos = []
valor = 2

while(len(primos) < 20):
    if primo(valor) == True:
        primos.append(int(valor))
    valor += 1

print (primos)
