"""
For a given a binary tree of integers and an X, find and return the total number of nodes of
given binary tree which are having data greater than X.
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
    binary_tree = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    binary_tree.left = left_tree
    binary_tree.right = right_tree
    return binary_tree


def greater_than_x(root, x):

    if root is None:
        return 0
    left_root = greater_than_x(root.left, x)
    right_root = greater_than_x(root.right, x)
    count = left_root + right_root
    if root.data > x:
        return 1 + count
    return count



r = take_input()
print(greater_than_x(r, 2))

