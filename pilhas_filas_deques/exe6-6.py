
def remove_elemento(vetor):
    if not vetor:
        return
    else:
        vetor.pop()
        remove_elemento(vetor)

vetor = [1,2,3,4]

remove_elemento(vetor)
