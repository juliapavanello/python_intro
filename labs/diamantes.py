def conta_diamantes(s: str) -> int:
    pilha = []
    count = 0
    for ch in s:
        if ch == '<':
            pilha.append(ch)
        elif ch == '>':
            if pilha:        
                pilha.pop()
                count += 1
    return count

# testes
print(conta_diamantes("<..><.<..>>"))      
print(conta_diamantes("< < <..<......< < < <....>"))  
