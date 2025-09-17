"""Helper functions to convert tuples to binary trees and vice versa, and to display the tree structure."""

from .base import TreeNode

#------------------------------------------------
# 1. Tuple to Binary Tree
#------------------------------------------------
def parse_tuple(data):
    """
    Converts a nested tuple representation of a binary tree into a TreeNode structure.
    Args:
        data (tuple): A nested tuple where each tuple is of the form (left_subtree, node_value, right_subtree).
    Returns
    """
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print(tree)  # Root node
    print(tree.key)  # Root value
    print(tree.left.key, tree.right.key)
    print(tree.left.left.key, tree.right.left.key, tree.right.right.key)  # Child nodes
    print(tree.right.left.right.key, tree.right.right.left.key, tree.right.right.right)  # Grandchild nodes

#------------------------------------------------
# 2. Binary Tree to Tuple
#------------------------------------------------
def tree_to_tuple(node):
    """
    Converts a TreeNode structure back into a nested tuple representation.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        tuple: A nested tuple representation of the binary tree.
    """
    if node is None: # empty node
        return None
    elif node.left is None and node.right is None: # leaf node
        return node.key
    else: # internal node
        tuple = (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right)) # recursive call; calling function inside itself until base case is reached
        return tuple

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("Original tuple:", tree_tuple)
    print("Converted back to tuple:", tree_to_tuple(tree))

#------------------------------------------------
# 3. Display Tree Structure
#------------------------------------------------
def display_keys(node, space='\t', level=0):
    """
    Displays the binary tree structure in a readable format.
    Args:
        node (TreeNode): The root of the binary tree.
        space (str): The string used for indentation (default is a tab character).
        level (int): Current level in the tree (used for indentation).
    """
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        return print(space * level + '∅')


    # If the node is a leaf
    elif node.left is None and node.right is None:
        return print(space * level + str(node.key))


    # If the node has children
    else:
        display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        display_keys(node.left, space, level + 1)

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("Tree structure:")
    display_keys(tree)

