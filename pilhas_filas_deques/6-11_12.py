from collections import deque
fila = deque()
fila.append(10)      # adiciona no final
fila.appendleft(5)   # adiciona no começo
fila.pop()           # remove do final
fila.popleft()       # remove do começo


class PilhaDeque:
    def __init__(self):
        self._deque = deque()

    def push(self, e):
        self._deque.append(e)

    def pop(self):
        return self._deque.pop()

    def top(self):
        self._deque[-1]


class FilaDeque:
    def __init__(self):
        self._deque = deque()

    def enqueue(self, e):
        self._deque.append(e)

    def dequeue(self):
        return self._deque.popleft()


