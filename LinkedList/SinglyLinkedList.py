class _Node:
    """Lightweight, nonpublic class for storing singly linked node."""
    __slots__ = '_element', '_next' #streamline memory usage

    def __init__(self, element, next):
        self._element = element
        self._next = next