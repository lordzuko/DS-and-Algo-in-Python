from DS.LinkedList.DoublyLinkedBase import _DoublyLinkedBase
from DS.Deque.Empty import Empty

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return(but do not remove) the element at the front end of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty()')
        return self._header._next._element # the first element is next to the header in DDL

    def last(self):
        """Return(but do not remove) the element at the end of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty()')
        return self._trailer._prev._element  # the last element is prev to the trailer in DDL

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e,self._header,self._header._next) # after header

    def insert_last(self,e):
        """Add an element to the end of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailers

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.delete_node(self._header._next)  #using inherited method

    def delete_last(self):
        """Remove and return the element from the end of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.delete_node(self._trailer._prev)  #using inherited method




