from DS.Queue.Empty import Empty

class CircularQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """
            Create an empty queue.
        """
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail.next
        return head._element

    def dequeue(self):
        """Removes the first element of the queue (i.e. FIFO)

        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty.')

        oldhead = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        """Add an element to the back of the queue."""
        newest = self._Node(e,None)

        if self.is_empty():
            self._tail = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  #old becomes the new tail

