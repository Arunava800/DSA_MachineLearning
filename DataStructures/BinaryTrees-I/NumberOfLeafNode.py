"""
Given a tree, return the number of leaf nodes.

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


def num_leaf_node(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    num_leaf_left = num_leaf_node(root.left)
    num_leaf_right = num_leaf_node(root.right)
    return num_leaf_left + num_leaf_right


r = take_input()
print(num_leaf_node(r))