class Empty(Exception):
    pass

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def _resize(self,cap):
        old_data = self._data
        self._data = [None] * cap
        walk = self._front

        for i in range(self._size):
            self._data[i] = old_data[walk]
            walk = (walk + 1) % len(old_data)

        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0<=self._size<=len(self._data)//4:
            self._resize(len(self._data)//2)

        return ans

    def enqueue(self,val):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = val
        self._size += 1

if __name__ == "__main__":
    Q = ArrayQueue()
    for i in range(10):
        Q.enqueue(i)
    Q.enqueue(11)
    print(Q.dequeue())
    print(Q.first())
    for i in range(8):
        print(Q.dequeue())

    print(Q.dequeue())
    print(Q.dequeue())
