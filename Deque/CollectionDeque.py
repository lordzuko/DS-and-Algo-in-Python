from collections import deque

class CollectionDeque:

    def __init__(self):
        self._data = deque()

    def add_first(self,e):
        self._data.appendleft(e)

    def add_right(self,e):
        self._data.append(e)

    def delete_first(self):
        return self._data.popleft()

    def delete_last(self):
        return self._data.pop()

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

if __name__ == "__main__":
    D = CollectionDeque()
    for i in range(10):
        D.add_first(i)

    print(D.delete_last())
    print(D.delete_first())
    print(D.first())
    print(D.last())