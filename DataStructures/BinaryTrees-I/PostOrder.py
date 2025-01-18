"""
For a given binary Tree, print the post order traversal.
sample input:
    1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1
sample Output:
    4 5 2 6 7 3 1
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
    binary_tree_data = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    binary_tree_data.left = left_tree
    binary_tree_data.right = right_tree
    return binary_tree_data


def print_detailed_data(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None:
        print("L", root.left.data, end=", ")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    print_detailed_data(root.left)
    print_detailed_data(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)

r = take_input()
print_detailed_data(r)
post_order(r)
