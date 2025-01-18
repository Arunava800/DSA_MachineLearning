"""
For a given Binary Tree of type integer and a number X, find whether a node exists
in the tree with data X or not.
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


def is_node_present(root, x):
    if root is None:
        return 0
    if root.data == x:
        return 1
    small_head_left = is_node_present(root.left, x)
    small_head_right = is_node_present(root.right, x)
    if small_head_left == 1 or small_head_right == 1:
        return True
    else:
        return False


r = take_input()
key = int(input())
t = is_node_present(r, key)
if t:
    print("True")
else:
    print("False")
