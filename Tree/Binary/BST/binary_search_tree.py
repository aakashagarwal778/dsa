import sys
if __name__ == "__main__":
    print(sys.path)
    sys.path.append('/Users/aakashagarwal/PyCharm/Resources/DSA/Tree')

from DSA.Tree.Binary.helper_functions import display_keys
from DSA.Tree.test_cases import users
from DSA.Tree.Binary.binary_tree import TreeNode

#--------------------------------------------------------------------
# Check if a Binary Tree is a Binary Search Tree (BST) & Min/Max Key
#--------------------------------------------------------------------
def remove_none(nums):
    """ Remove None values from a list"""
    return [x for x in nums if x is not None]


def is_bst(node):
    """
    Checks if a binary tree is a binary search tree (BST) i.e., left < root < right.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        tuple: A tuple containing:
            - bool: True if the tree is a BST, False otherwise.
            - min_key: The minimum key in the tree.
            - max_key: The maximum key in the tree.
    """
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and                  # Both left and right subtrees must be BST
                   (max_l is None or node.key > max_l) and    # Current node must be greater than max in left subtree
                   (min_r is None or node.key < min_r))       # Current node must be less than min in right subtree

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key


if __name__ == "__main__":

    # Example usage
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode.parse_tuple(tree_tuple)
    display_keys(tree)
    print("Is BST:", is_bst(tree)[0])
    print("Min Key: {}, Max Key: {}".format(is_bst(tree)[1], is_bst(tree)[2]))

    tree_tuple2 = (('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal'))
    tree2 = TreeNode.parse_tuple((tree_tuple2))
    display_keys(tree2)
    print("Is BST:", is_bst(tree2)[0])
    print("Min Key: {}, Max Key: {}".format(is_bst(tree2)[1], is_bst(tree2)[2]))


#----------------------------------------------
# Storing Key-Value Pairs in BST
#----------------------------------------------
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

if __name__ == "__main__":
    # Example usage
    # users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    # Level 0
    jadhesh = users[3]
    tree = BSTNode(jadhesh.username, jadhesh)
    print(tree.key, tree.value)

    # Level 1
    biraj = users[1]
    sonaksh = users[5]
    tree.left = BSTNode(biraj.username, biraj)
    tree.right = BSTNode(sonaksh.username, sonaksh)
    print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

    # Level 2
    aakash = users[0]
    hemanth = users[2]
    siddhant = users[4]
    vishal = users[6]
    tree.left.left = BSTNode(aakash.username, aakash)
    tree.left.right = BSTNode(hemanth.username, hemanth)
    tree.right.left = BSTNode(siddhant.username, siddhant)
    tree.right.right = BSTNode(vishal.username, vishal)
    print(tree.left.left.key, tree.left.left.value, tree.left.right.key, tree.left.right.value,
          tree.right.left.key, tree.right.left.value, tree.right.right.key, tree.right.right.value)

    display_keys(tree)


