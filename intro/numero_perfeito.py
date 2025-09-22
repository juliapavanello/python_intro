import sys

n = int(sys.argv[1])

resultado = False

def perfeito(valor):
    soma = 1
    divisores = '1 '
    for i in range(2, valor):
        if (valor % i) == 0:
            soma += i
            divisores += str(i) + ' '
    return valor == soma, divisores

resultado, divisores = perfeito(n)

if resultado:
    print(f'{n} é perfeito')
else:
    print(f'{n} não é perfeito')


print(f'Divisores: {divisores}')