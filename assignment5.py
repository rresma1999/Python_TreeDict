"""Implement a class called TreeDict that supports operators the same
way as a dict. 

TreeDict should be implemented using the binarysearchtree module I
have provided (you can download it from canvas in the same folder as
this file).

You need to make sure you support the following operations with the
same semantics as a normal Python dict:
* td[key]
* td[key] = value
* key in td
* td.get(key)
* td.get(key, default)
* td.update(iterable_of_pairs_or_dict_or_TreeDict)
* len(td)
* for key in td: pass
* for key, value in td.items(): pass
* A constructor: TreeDict(iterable_of_pairs_or_dict_or_TreeDict)

Iteration should be in key order, this should be pretty easy to do
just by traversing the tree using an in-order traversal. None of the
iterator methods should make a copy of any of the data in the
TreeDict. You should only implement in-order traversal once and use
that implementation for both kinds of traversal.

You should support a constructor which takes the same arguments as
update and creates a TreeDict with just those values. There is an easy
way to do this in just a couple of lines using your existing update
method.

For each operation, make sure it does the same thing as a dict and you
handle errors by throwing the same type of exception as would be
thrown by a dict. However you only need to handle the operations
listed above, not all operations supported by dict. Unlike dict your
implementation will not support None as a key and you should throw an
appropriate exception if None is used as a key. Look at the available
built in exceptions and pick the most appropriate one you find.

Most of these methods will be very short (just a couple of lines of
code), a couple will be a bit more complicated. However all the hard
work should already be handled by the binarysearchtree module. It
looks like a lot of operations, but it shouldn't actually take that
long. Many of the operations are quite similar as well.

Do not reimplement anything in the binarysearchtree module or copy
code from it. You should not need to.

For this assignment I expect you will have to use at least the
following things you have learned:
* Raising exceptions
* Catching exceptions
* Implementing magic methods
* Generators using yield (and you will need to look up "yield from" in the Python documentation)
* Type checks
* Default values/optional arguments

You will also need to read code which I think will help you learn to
think in and use Python.

To reiterate some of the things you should be aware of to avoid losing
points:
* None of the iterator methods should make a copy of any of the data
  in the TreeDict.
* You should only implement in-order traversal once and it should be
  recursive (it's so much easier that way).
* Do not reimplement anything in the binarysearchtree module or copy
  code from it.
* There are easy ways to implement all the required operations. If
  your implementation of a method is long you may want to think if
  there is a simpler way.

Links:
* https://docs.python.org/3.5/library/stdtypes.html#dict
* http://en.wikipedia.org/wiki/Binary_search_tree#Traversal
* https://docs.python.org/3.5/reference/expressions.html#yieldexpr

"""

import binarysearchtree as bst


class TreeDict(object):
    """A representation of a TreeDictionary that stores sorted (Key, Value) pairs

    Supports the same operators of those of a regular dict
    """

    # TODO: handle all three cases of data being an iterable of pairs, a dict, or a Tree Dict
    def __init__(self, data=None):
        """Constructor for our TreeDict Class.

        Instance attributes: root Node

        Instantiates a new Tree Dictionary, based on the data passed into the constructor. Data could be anything from
        a regular dict, an iterable of pairs, or another TreeDict
        """
        self.root = None
        # Default empty constructor
        if data is None:
            self.root = bst.Node()
        # Regular dict or a TreeDict passed into the constructor
        elif isinstance(data, dict) or isinstance(data, TreeDict):
            for k, v in data.items():
                self._tree_insert(k, v)
        # Must be an iterable of pairs
        elif hasattr(data, "__iter__"):
            # Iterate through each of the pairs
            for elem in data:
                # Iterable input must be in pairs
                if len(elem) == 2 and hasattr(elem, "__iter__"):
                    self._tree_insert(elem[0], elem[1])
                else:
                    raise TypeError("Incorrect input format: iterable of pairs")
        # Incorrect input to the constructor
        else:
            raise TypeError("Incorrect input format: must either be an iterable of pairs, a dict, or another TreeDict")

    def _tree_insert(self, key, value):
        """Helper method for the constructor for TreeDict Class to help build the underlying BST
        """
        # Initially empty BST
        if self.root is None:
            self.root = bst.Node(key, value)
        # Otherwise, Insert the nodes at the correct spots based on the root
        self.root.insert(key, value)

    def __getitem__(self, key):
        """Access method for our TreeDict Class.

        Ex: td[key]

        Return the item of td with key 'key'. Raises a KeyError if key is not in the map.
        """
        # Utilize our BST lookup function to traverse the tree based key comparisons to the current node
        try:
            return self.root.lookup(key).value
        except ValueError:
            raise KeyError(f"Key {repr(key)} is not in the TreeDict")

    def __setitem__(self, key, value):
        """Set method for our TreeDict Class.

        Ex: td[key] = value

        Set td[key] to value.
        """
        # Utilize our BST insert function to either set, or insert a new (key, value) pair
        self.root.insert(key, value)

    def __contains__(self, key):
        """Contains method for our TreeDict Class.

        Ex: key in td

        Return True if td has a key 'key', else False."""
        try:
            if self.root.lookup(key):
                return True
        except ValueError:
            return False

    def __len__(self):
        """Length method for the TreeDict Class.

        Ex: len(td)

        Return the number of items in the dictionary td.
        """
        # Empty or Null TreeDict
        if not self.root or self.root.key is None:
            return 0
        # Otherwise count all the nodes with a traversal
        else:
            return sum(1 for node in self.items())

    def get(self, key, default=None):
        """Get method for the TreeDict Class.

        Ex: td.get(key)

        Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None,
        so that this method never raises a KeyError."""
        if key is not None:
            try:
                # Regular TreeDict access
                return self.root.lookup(key).value
            except ValueError:
                # Instead of returning a Key or Value Error, return default
                return default
        else:
            raise KeyError("None-value key passed to get()")

    def update(self, data=None):
        """Update method for our TreeDict Class.

        Ex: td.update(iterable_or_dict_or_TreeDict)

        Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
        update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other
        iterables of length two). Lastly update() may accept another TreeDict instance
        """
        # Only modify our TreeDict if data is non-Null
        if data:
            # Case where data is either a dict or a TreeDict
            if isinstance(data, dict) or isinstance(data, TreeDict):
                # Iterate through our data's (K, V) pairs, updating our TreeDict as needed
                for k1, v1 in data.items():
                    self.__setitem__(k1, v1)
            # Case where data is simply an iterable of pairs
            elif hasattr(data, "__iter__"):
                # Iterate through each of the pairs
                for elem in data:
                    # Iterable input must be in pairs
                    if len(elem) == 2 and hasattr(elem, "__iter__"):
                        self.__setitem__(elem[0], elem[1])
                    else:
                        raise TypeError("Incorrect input format: iterable of pairs")
            # Case where data is in the incorrect form
            else:
                raise TypeError("Incorrect input format: must either be an iterable of pairs, a dict, or TreeDict")
        else:
            raise ValueError("NoneType object passed to update()")

    def items(self):
        """Method to return a generator of tuples containing the (key, value) pairs of every node
         contained in the TreeDict

        Ex: td.items()
        """
        if self.root:
            return ((node.key, node.value) for node in self._traverse_binary_tree(self.root) if node)
        else:
            return (iter(()))

    def keys(self):
        """Method to return a generator of the values contained in the TreeDict

        Ex: td.keys()
        """
        if self.root:
            return (node.key for node in self._traverse_binary_tree(self.root) if node)
        else:
            return iter(())

    def values(self):
        """Method to return a generator of the values contained in the TreeDict

        Ex: td.values()
        """
        if self.root:
            return (node.value for node in self._traverse_binary_tree(self.root) if node)
        else:
            return iter(())

    def __iter__(self):
        """Iter method for our TreeDict Class.

        Return an iterator over the keys of the dictionary. This is a shortcut for iter(td.keys())
        """
        return self.keys()

    def _traverse_binary_tree(self, node):
        """In-order-traversal of a Binary Search Tree.

        Traverses the tree in order to return the elements sorted from least to greatest.
        Code given by Dr. Arthur Peters from Wikipedia
        https://en.wikipedia.org/wiki/Binary_search_tree#Traversal
        """
        # Yield Left Branch nodes
        yield from self._traverse_binary_tree(node.left) if node.left else ()
        yield node
        # Yield Right Branch nodes
        yield from self._traverse_binary_tree(node.right) if node.right else ()
