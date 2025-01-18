"""
For a given Binary Tree of integers, find and return the height of the tree. Height
is defined total number of nodes along the longest path from the root to any of the leaf node.
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    root_data = int(input())
    if root_data == -1:
        return None
    tree = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    tree.left = left_tree
    tree.right = right_tree
    return tree


def height_of_tree(root):
    if root is None:
        return 0
    left_root = height_of_tree(root.left)
    right_root = height_of_tree(root.right)
    count = max(left_root, right_root)
    return 1 + count


r = take_input()
print(height_of_tree(r))

