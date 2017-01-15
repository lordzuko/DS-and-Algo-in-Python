from DS.PriorityQueue.PriorityQueueBase import PriorityQueueBase
from DS.PriorityQueue.Empty import Empty

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list.

    Operation  TimeComplexity
    len             O(1)
    is_empty        O(1)
    add             O(n)
    min             O(1)
    remove_min      O(1)
    """

    def __init__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = walk._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (K,V) tuple iwth minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

