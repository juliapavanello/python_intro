def transfer(vetor1, vetor2):
    while vetor1:
        vetor2.append(vetor1.pop())


s = [1,2,3]
t = []
transfer (s, t)
print(s)
print(t)