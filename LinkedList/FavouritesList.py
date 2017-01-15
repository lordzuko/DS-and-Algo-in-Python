from DS.LinkedList.PositionalList import PositionalList

class FavouritesList:
    """List of elements ordered from most frequently accessed to least."""

    #------------------nested _Item class--------------------------#
    class _Item:
        __slots__ = '_value', '_count'  #streamline memory usage

        def __init__(self, e):
            self._value = e         #the user's element
            self._count = 0         #access count initially zero

    #------------------nonpublic utilities-------------------------#
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk._element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))


    #------------------public methods------------------------------#
    def __init__(self):
        """Create an empty list of favourites."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of entries in the favourite list."""
        return len(self._data)

    def is_empty(self):
        """Return True if the list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element, thereby increasing it access count."""
        p = self._find_position(e)      # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e)) # if new, place at the end of list
        p.element()._count += 1     # always increment count
        self._move_up(p)        # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favourites."""
        p = self._find_position(e)      # try to locate existing element
        if p is not None:
            self._data.delete(p)        # delete, if found

    def top(self, k):
        """Generate a sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal Value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()       # element of list is _Item
            yield item._value
            walk = self._data.after(walk)


