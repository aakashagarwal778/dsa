"""Encapsulation of data and methods (helper functions & traversal functions) for a binary tree."""

from .helper_functions import display_keys

class TreeNode():
    """
    A class representing nodes in a binary tree encapsulating various utility methods.
    Attributes:
        key: The value or key of the node.
        left: A pointer/reference to the left child node.
        right: A pointer/reference to the right child node.
    Methods:
        height(): Returns the height of the tree.
        size(): Returns the total number of nodes in the tree.
        traverse_in_order(): Returns a list of keys in in-order traversal.
        traverse_pre_order(): Returns a list of keys in pre-order traversal.
        traverse_post_order(): Returns a list of keys in post-order traversal.
        display_keys(space='\t', level=0): Displays the tree structure visually.
        to_tuple(): Converts the tree into a nested tuple representation.
        parse_tuple(data): Static method to create a tree from a nested tuple representation.
    """
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    def traverse_pre_order(self):
        if self is None:
            return []
        return ([self.key] +
                TreeNode.traverse_pre_order(self.left) +
                TreeNode.traverse_pre_order(self.right))

    def traverse_post_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_post_order(self.left) +
                TreeNode.traverse_post_order(self.right) +
                [self.key])

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

            # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

if __name__ == "__main__":
    # Example usage
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode.parse_tuple(tree_tuple)
    print("Tree Height:", tree.height())
    print("Tree Size:", tree.size())
    print("In-order Traversal:", tree.traverse_in_order())
    print("Pre-order Traversal:", tree.traverse_pre_order())
    print("Post-order Traversal:", tree.traverse_post_order())
    print("Tree to Tuple:", tree.to_tuple())
    print(tree)  # Root node
    print(tree.key)  # Root value
    print(tree.left.key, tree.right.key)
    print(tree.left.left.key, tree.right.left.key, tree.right.right.key)  # Child nodes
    print(tree.right.left.right.key, tree.right.right.left.key, tree.right.right.right)  # Grandchild nodes
    tree.display_keys()