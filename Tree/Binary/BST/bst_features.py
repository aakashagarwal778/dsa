"""
This module implements various features of a Binary Search Tree (BST) including:
1. Inserting a node
2. Finding a node
3. Updating a node
4. Listing all nodes
5. Checking if the tree is balanced
6. Creating a balanced BST from sorted data
7. Balancing an unbalanced BST

It uses a BSTNode class from binary_search_tree.py to represent each node in the tree
and includes helper functions for displaying the tree and calculating its height.
"""


import sys
if __name__ == "__main__":
    print(sys.path)
    sys.path.append('/Users/aakashagarwal/PyCharm/Resources/DSA/Tree')

from DSA.Tree.test_cases import *
from binary_search_tree import BSTNode
from DSA.Tree.Binary.helper_functions import display_keys
from DSA.Tree.Binary.traversal import tree_height

#------------------------------------------------
# 1. Insert Node in a Binary Search Tree (BST)
#------------------------------------------------
def insert(node, key, value):
    """
    Inserts a new node with the given key and value into the BST.
    Args:
        node (BSTNode): The root of the BST.
        key: The key of the new node.
        value: The value associated with the key.
    Returns:
        BSTNode: The root of the updated BST.
    """
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

if __name__ =="__main__":
    # Example 1: Balanced BST
    #users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    tree = insert(None, jadhesh.username, jadhesh) # Root node
    # Child nodes
    insert(tree, biraj.username, biraj)
    insert(tree, sonaksh.username, sonaksh)
    insert(tree, aakash.username, aakash)
    insert(tree, hemanth.username, hemanth)
    insert(tree, siddhant.username, siddhant)
    insert(tree, vishal.username, siddhant)

    display_keys(tree)
    print("Height of tree1: {}".format(tree_height(tree)))

    # Example 2: Unbalanced/Skewed BST i.e., Order of insertion matters
    tree2 = insert(None, aakash.username, aakash)
    insert(tree2, biraj.username, biraj)
    insert(tree2, hemanth.username, hemanth)
    insert(tree2, jadhesh.username, jadhesh)
    insert(tree2, siddhant.username, siddhant)
    insert(tree2, sonaksh.username, sonaksh)
    insert(tree2, vishal.username, vishal)

    display_keys(tree2)
    print("Height of tree2: {}".format(tree_height(tree2)))

#------------------------------------------------
# 2. Find Node in a Binary Search Tree (BST)
#------------------------------------------------
def find(node, key):
    """
    Finds a node with the given key in the BST.
    Args:
        node (BSTNode): The root of the BST.
        key: The key to search for.
    Returns:
        BSTNode or None: The node with the specified key, or None if not found.
    """
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

if __name__ == "__main__":
    # Example usage
    user_node = find(tree, 'siddhant')
    print(user_node)
    print("Key: {}, Value: {}".format(user_node.key, user_node.value))

#------------------------------------------------
# 3. Update Node in a Binary Search Tree (BST)
#------------------------------------------------
def update(node, key, value):
    """
    Updates the value of a node with the given key in the BST.
    Args:
        node (BSTNode): The root of the BST.
        key: The key of the node to update.
        value: The new value to set.
    Returns:
        None
    """
    target = find(node, key)
    if target is not None:
        target.value = value

if __name__ == "__main__":
    update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
    node = find(tree, 'hemanth')
    print("Key: {}, Updated Value: {}".format(node.key, node.value))

#------------------------------------------------
# 4. List All Nodes in a Binary Search Tree (BST)
#------------------------------------------------
def list_all(node):
    """
    Lists all key-value pairs in the BST in sorted order.
    """
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

if __name__ == "__main__":
    all_users = list_all(tree)
    for key, value in all_users:
        print("Key: {}, Value: {}".format(key, value))

#------------------------------------------------
# 5. Check if a Binary Search Tree (BST) is Balanced
#------------------------------------------------
def is_balanced(node):
    """
    Checks if the BST is balanced by verifying that the heights of the two child subtrees
    of any node differ by no more than one.
    Args:
        node (BSTNode): The root of the BST.
    Returns:
        tuple: A tuple containing:
            - bool: True if the tree is balanced, False otherwise.
            - int: The height of the tree.
    """
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left) # Check left subtree
    balanced_r, height_r = is_balanced(node.right) # Check right subtree
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1 # Current node
    height = 1 + max(height_l, height_r) # Height of current node
    return balanced, height

if __name__ == "__main__":
    balanced, height = is_balanced(tree)
    print("Is tree1 balanced?: {}, Height: {}".format(balanced, height))

    balanced2, height2 = is_balanced(tree2)
    print("Is tree2 balanced?: {}, Height: {}".format(balanced2, height2))

#------------------------------------------------
# 6. Create a Balanced Binary Search Tree (BST) from Sorted Data
#------------------------------------------------
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    """
    Creates a balanced BST from sorted list/key-value pairs
    Args:
        data (list): A sorted list of tuples where each tuple is of the form (key, value).
        lo (int): The lower index of the current sublist.
        hi (int): The higher index of the current sublist.
        parent (BSTNode): The parent node of the current subtree.
    Returns:
        BSTNode: The root of the balanced BST.
    """
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root

if __name__ == "__main__":
    data = [(user.username, user) for user in users]
    print(data)
    balanced_tree = make_balanced_bst(data)
    display_keys(balanced_tree)

#------------------------------------------------
# 7. Balance an Unbalanced Binary Search Tree (BST)
#------------------------------------------------
def balance_bst(node):
    """
    Balances an unbalanced BST by first listing all its elements in sorted order
    and then reconstructing a balanced BST from that sorted list.
    Args:
        node (BSTNode): The root of the unbalanced BST.
    Returns:
        BSTNode: The root of the balanced BST.
    """
    return make_balanced_bst(list_all(node))

if __name__ == "__main__":
    tree1 = None

    for user in users:
        tree1 = insert(tree1, user.username, user)

    display_keys(tree1)
    print("Is tree1 balanced?: {}".format(is_balanced(tree1)[0]))

    balanced_tree1 = balance_bst(tree1)
    display_keys(balanced_tree1)
    print("Is balanced_tree1 balanced?: {}".format(is_balanced(balanced_tree1)[0]))



