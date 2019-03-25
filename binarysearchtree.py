"""An implementation of a binary search tree.

Read and understand this code. This is part of the assignment so don't
ask for outside help with this specific code or discuss this code with
class mates. However, feel free to look things up or discuss general
concepts to help you understand what you are reading.

You may find it useful to add comments and documentation to this file
as you go. However do not change the code in this module in any way. I
will be testing with my own version.

NOTE: This code is intentionally uncommented to force you to read and
understand it. However it is not obfuscated in any way. That being
said if you were to write something like this you should comment
it. It does need comments to make it easier to work with.

"""

class Node(object):
    # Our encapsulated data for the Node: it is either a left and a right child, has a key and a value for hashing
    __slots__ = ("left", "right", "key", "value")

    """Constructor for Node Class.
    
    Instantiates an empty node with specified key and value, None if unspecified.
    """
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    """Recursive, Helper method for the Insert method for Node Class.
    
    Triggers a recursive call to insert (specified for traversing either the left or right branch of the current
    child) to find the slot to add the current node.
    """
    @classmethod
    def _insert_in_child(cls, child, key, value):
        if child:
            return child, child.insert(key, value)
        else:
            node = cls(key, value)
            return node, node

    """Insert method for Node Class.
    
    Adds a new node to the BST, in order, meaning that the value passed into the new Node determines placement.
    In any BST, lesser values go to the right child and greater values go to the right
    """
    def insert(self, key, value):
        # Null check
        if key is None:
            raise ValueError("None cannot be used as a key")
        # Non-empty dict case
        if self.key is not None:
            # Try insert in Left branch
            if key < self.key:
                self.left, ret = self._insert_in_child(self.left, key, value)
            # Try insert in Right branch
            elif key > self.key:
                self.right, ret = self._insert_in_child(self.right, key, value)
            # Key already exists in the dict, simply modify the Value
            else:
                self.value = value
                ret = self
            return ret
        # Empty dict case
        else:
            self.key = key
            self.value = value
            return self

    """Recursive static Helper function for the Lookup method for Node Class.
    
    Triggers a recursive call to the lookup function to traverse either left or right to find the specified node.
    """
    @staticmethod
    def _lookup_in_child(child, key):
        # Null Check
        if child:
            return child.lookup(key)
        else:
            raise ValueError("Key not in tree: " + repr(key)) 

    """Lookup method for the Node Class.
    
    Starts at given node, then traverses either left or right depending on the current (key, value) pair being 
    evaluated.
    """
    def lookup(self, key):
        # Null Check
        if key is None:
            raise ValueError("None cannot be used as a key")
        # Key does not exist
        if self.key is None:
            raise ValueError("Key not in tree: " + repr(key))
        # Try to lookup key in the Left branch
        if key < self.key:
            return self._lookup_in_child(self.left, key)
        # Try to lookup key in the Right branch
        elif key > self.key:
            return self._lookup_in_child(self.right, key)
        # We have found the key if ==
        else:
            return self

    """Recursive Helper method for the Delete method for Node Class.
    
    Traverses the BST, searching by Key, for the (Key, Value) Pair to be removed from the BST.
    """
    def _delete_internal(self, key, parent):
        # Traverse Left branch
        if key < self.key:
            self.left._delete_internal(key, self)
        # Traverse Right branch
        elif key > self.key:
            self.right._delete_internal(key, self)
        # We have found the potential Node to be removed
        else:
            if self.left and self.right:
                n, parent = self._next_descendant()
                self.key, self.value = n.key, n.value
                n._delete_internal(n.key, parent)
            elif self.left or self.right:
                child = self.left or self.right
                self.key, self.value = child.key, child.value
                self.left, self.right = child.left, child.right
            else:
                if parent:
                    if parent.left is self:
                        parent.left = None
                    elif parent.right is self:
                        parent.right = None
                    else:
                        raise RuntimeError("Bug in BST implementation: parent "
                                           "does not have self as a child")
                else:
                    self.key = None
                    self.value = None

    """Delete method for the Node Class.
    
    Recursively traverses tree, searching by key, to find the (Key, Value) pair to be removed from the BST
    """
    def delete(self, key):
        if key is None:
            raise ValueError("None cannot be used as a key")
        self._delete_internal(key, None)

    def _next_descendant(self):
        parent = self
        n = self.right
        if not n:
            return None, parent
        while n.left:
            parent, n = n, n.left
        return n, parent

    def min_child(self):
        n = self.left
        if not n:
            return self
        while n.left:
            n = n.left
        return n
