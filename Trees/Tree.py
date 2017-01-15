from DS.LinkedList.LinkedQueue import LinkedQueue

class Tree:
    """Abstract base class representing a tree structure."""

    def __iter__(self):
        """Generate an iteration of tree's elements."""
        for p in self.positions():
            yield p.element()

    #----------------------nested position class------------------------#
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError('Must be implemented by the subclass')

        def __eq__(self, other):
            """Return True if the other position refers the same location."""
            raise NotImplementedError('Must be implemented by the subclass')

        def __ne__(self, other):
            """Return True if the other position doesn't refer the same location."""
            raise NotImplementedError('Must be implemented by the subclass')

    #-------Abstract methods  that concrete subclass must support---------#

    def root(self):
        """Return  Position representing the tree's root(or None if empty)"""
        raise NotImplementedError('Must be implemented by the subclass')

    def parent(self, p):
        """Return Positioon representing p's parent (or None if p is root)"""
        raise NotImplementedError('Must be implemented by the subclass')

    def num_children(self, p):
        """Return the number of children that p has"""
        raise NotImplementedError('Must be implemented by the subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's position."""
        raise NotImplementedError('Must be implemented by the subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('Must be implemented by the subclass')

    #--------Concrete methods implemented in this class---------------#
    def is_root(self, p):
        """Return True if p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if p doesn't have children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty"""
        return len(self) == 0

    def _height2(self, p):
        """Return the height of subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    #-------------------- Traversal methods -----------------------------------#
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                         # visit p before its subtrees
        for c in self.children(p):                      # for each child c
            for other in self._subtree_preorder(c):     # do preorder of c's subtree
                yield other                             # yield each of our caller

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def position(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        """Generate a postorder iterations of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()              #know positions not yet yielded
            fringe.enqueue(self.root())         #starting with the root
            while not filter.is_empty():
                p = fringe.dequeue()            #remove the front of the queue
                yield p                         #report this position
                for c in self.children(p):
                    fringe.enqueue(c)           #add children to back of queue










