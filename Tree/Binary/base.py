""" Binary Tree Node Base Implementation """

class TreeNode:
    """
    A class representing nodes in a binary tree.
    Attributes:
        key: The value or key of the node.
        left: A pointer/reference to the left child node.
        right: A pointer/reference to the right child node.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


if __name__ == "__main__":
    # Example usage

    # Create nodes
    node0 = TreeNode(3)
    node1 = TreeNode(4)
    node2 = TreeNode(5)

    # root node
    print(node0)
    print(node0.key)

    # child nodes
    node0.left = node1
    node0.right = node2

    # print the tree structure
    tree = node0
    print(tree.key)
    print(tree.left.key)
    print(tree.right.key)


