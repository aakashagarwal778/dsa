import sys
if __name__ == "__main__":
    print(sys.path)
    sys.path.append('/Users/aakashagarwal/PyCharm/Resources/DSA/Tree/')

from bst_features import insert, find, update, list_all, display_keys, balance_bst
from DSA.Tree.Binary.traversal import tree_size

class TreeMap():
    """
    A TreeMap implementation using a balanced Binary Search Tree (BST).
    This class provides dictionary-like functionality with efficient
    insertion, retrieval, and iteration over key-value pairs.

    Attributes:
        root (BSTNode): The root node of the BST.
    Methods:
        __setitem__(key, value): Inserts or updates a key-value pair.
        __getitem__(key): Retrieves the value associated with a key.
        __iter__(): Iterates over all key-value pairs in sorted order.
        __len__(): Returns the number of key-value pairs in the TreeMap.
        display(): Displays the structure of the BST.
    """
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value): # i.e., key: aakash = value: User()
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)

if __name__ == "__main__":

    from DSA.Tree.test_cases import *
    treemap = TreeMap()
    treemap.display()

    treemap['aakash'] = aakash
    treemap['jadhesh'] = jadhesh
    treemap['sonaksh'] = sonaksh
    treemap['biraj'] = biraj
    treemap['hemanth'] = hemanth
    treemap['siddhant'] = siddhant
    treemap['vishal'] = vishal

    treemap.display()
    print('Length:{}'.format(len(treemap)))

    for index, (key, value) in enumerate(treemap):
     print('{}. key:{}, value:{}'.format(index + 1, key, value))

    list(treemap)
    print('List of all keys:', list(treemap))

    treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
    print('Updated aakash:', treemap['aakash'])