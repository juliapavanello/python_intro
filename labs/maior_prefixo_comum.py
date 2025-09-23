import random
import time

# ---------------------------------
# Gerador de instâncias
# ---------------------------------
def gerar_instancia(N):
    base = ''.join(random.choice("ABCD") for _ in range(random.randint(5, 10)))
    vetor = []
    for _ in range(N):
        s = list(base)
        for i in range(len(s)):
            if random.random() < 0.3: 
                s[i] = random.choice("ABCD")
        vetor.append(''.join(s))
    return vetor



# Abordagem 1 (comparação char a char)

def maior_prefixo_1(vetor):
    if not vetor:
        return ""
    pref = ""
    for i in range(len(vetor[0])):   
        aux = vetor[0][i]        
        for j in range(len(vetor)):
            if i >= len(vetor[j]) or aux != vetor[j][i]:
                return pref
        pref += aux
    return pref



# Abordagem 2 (ordenar e comparar primeira e última)

def maior_prefixo_2(vetor):
    if not vetor:
        return ""
    vetor_ordenado = sorted(vetor)
    pref = ""
    for i in range(len(vetor_ordenado[0])):
        if vetor_ordenado[0][i] == vetor_ordenado[-1][i]:
            pref += vetor_ordenado[0][i]
        else:
            break
    return pref



# Testes 
def rodar_testes():
    print(f"{'N':<10}{'Tempo A1 (s)':<20}{'Tempo A2 (s)':<20}")
    for exp in range(1, 21):  # de 2^1 até 2^20
        N = 2 ** exp
        vetor = gerar_instancia(N)

        # Abordagem 1
        inicio = time.time()
        maior_prefixo_1(vetor)
        tempo_a1 = time.time() - inicio

        # Abordagem 2
        inicio = time.time()
        maior_prefixo_2(vetor)
        tempo_a2 = time.time() - inicio

        print(f"{N:<10}{tempo_a1:<20.6f}{tempo_a2:<20.6f}")


# -------------------------------
# Executar
# -------------------------------
if __name__ == "__main__":
    rodar_testes()
