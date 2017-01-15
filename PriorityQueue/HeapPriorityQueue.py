from DS.PriorityQueue.PriorityQueueBase import PriorityQueueBase
from DS.PriorityQueue.Empty import Empty

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap.

    Operation       Time Complexity
    len(P)              O(1)
    P.is_empty()        O(1)
    P.min()             O(1)
    P.add()             O(log n) -> amortized
    P.remove_min()      O(log n) -> amortized

    """
    #--------------------non-public behaviors-----------------------#
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)      #index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)     #index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)

    #--------------------------- public behaviours ----------------------#
    def __init__(self, contents=()):
        """Create a new empty Priority Queue."""
        self._data = [self._Item(k,v) for k,v in contents]      #empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self._data)-1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data)-1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty Exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is Empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """

        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0,len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
