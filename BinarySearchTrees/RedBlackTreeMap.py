from DS.BinarySearchTrees.TreeMap import TreeMap

class RedBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree."""

    class _Node(TreeMap._Node):
        """Node class for red-black tree maintains bit that denotes color."""
        __slots__ = '_red'                          # add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True                        # new node red by default

    #-------------------- positional-based utility methods ------------------#
    def _set_red(self, p): p._node._red = True
    def _set_black(self, p): p._node._red = False
    def _set_color(self, p, make_red): p._node._red = make_red
    def _is_red(self, p): return p is not None and p._node._red
    def _is_red_leaf(self): return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """Return a red child of p (or None if no such child)."""
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    #-------------------- support for insertions ----------------------------#
    def _rebalance_insert(self, p):
        self._resolve_red(p)                        # new node is always red

    def _resolve_red(self, p):
        if self.is_root(p):
            self._set_black(p)                      # make root black
        else:
            parent = self.parent(p)
            if self._is_red(parent):                # double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):         # Case 1: misshapen 4-node
                    middle = self._restructure(p)   # do trinode restructuring
                    self._set_black(middle)         # then fix-color
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:                               # Case 2: overall five node
                    grand = self.parent(parent)
                    self._set_red(grand)            # grand parent becomes red
                    self._set_black(self.left(grand))   # its children becomes black
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)        # recur at red grandparent
