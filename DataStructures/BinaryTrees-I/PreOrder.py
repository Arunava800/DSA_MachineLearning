"""
You are given the root node of a binary tree. Print its preorder traversal.
Sample Input:
 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output:
    1 2 4 5 3 6 7
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


def print_pre_order(root):
    if root is None:
        return
    print(root.data, end=" ")
    if root.left is not None:
        print_pre_order(root.left)
    if root.right is not None:
        print_pre_order(root.right)


r = take_input()
print_detailed_data(r)
print_pre_order(r)
