from DS.Trees.Tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing binary tree sturucture."""

    #------additional abstract methods------------------#
    def left(self, p):
        """Return a position representing P's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a position representing P's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    #-------------concrete methods implemented in this class ---------------#
    def sibling(self, p):
        """Return a position representing p's sibling(or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:      # if p is root
            return None         # root doesn't have any sibling
        else:
            if p == self.left(parent): #if p is left child
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of positions of p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    #----------------------Traversal methods --------------------------#
    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        """Generate an inorder iteration of positons in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    #override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()       # make inorder the default
