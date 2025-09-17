"""Binary Tree Traversal and Properties such as height and size."""

from .helper_functions import parse_tuple, display_keys

#------------------------------------------------
# 1. In-Order Traversal
#------------------------------------------------
def traverse_in_order(node):
    """
    Performs an in-order traversal of the binary tree i.e., left-root-right.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        list: A list of node keys in in-order sequence.
    """
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("In-order Traversal:", traverse_in_order(tree))
    display_keys(tree)

#------------------------------------------------
# 2. Pre-Order Traversal
#------------------------------------------------
def traverse_pre_order(node):
    """
    Performs a pre-order traversal of the binary tree i.e., root-left-right.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        list: A list of node keys in pre-order sequence.
    """
    if node is None:
        return []
    return([node.key] +
           traverse_pre_order(node.left) +
           traverse_pre_order(node.right))

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("Pre-order Traversal:", traverse_pre_order(tree))
    display_keys(tree)

#------------------------------------------------
# 3. Post-Order Traversal
#------------------------------------------------
def traverse_post_order(node):
    """
    Performs a post-order traversal of the binary tree i.e., left-right-root.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        list: A list of node keys in post-order sequence.
    """
    if node is None:
        return []
    return(traverse_post_order(node.left) +
           traverse_post_order(node.right) +
           [node.key])

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("Post-order Traversal:", traverse_post_order(tree))
    display_keys(tree)

#------------------------------------------------
# 4. Tree Height
#------------------------------------------------
def tree_height(node):
    """
    Calculates the height of the binary tree.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        int: The height of the tree. Height of an empty tree is 0.
    """
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right)) # 1 for the current node

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    print("Tree Height:", tree_height(tree))
    display_keys(tree)

#------------------------------------------------
# 5. Tree Size
#------------------------------------------------
def tree_size(node):
    """
    Calculates the size (number of nodes) of the binary tree.
    Args:
        node (TreeNode): The root of the binary tree.
    Returns:
        int: The size of the tree. Size of an empty tree is 0.
    """
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right) # 1 for the current node