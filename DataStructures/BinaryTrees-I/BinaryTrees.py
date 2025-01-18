"""
------------------------------BINARY  TREES -----------------------------------------
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)


def print_tree_detailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    print_tree_detailed(root.left)
    print_tree_detailed(root.right)


def take_input():
    root_data = int(input())
    root = BinaryTree(root_data)
    if root_data == -1:
        return None
    left_tree = take_input()
    right_tree = take_input()
    root.left = left_tree
    root.right = right_tree
    return root


btn1 = BinaryTree(1)
btn2 = BinaryTree(4)
btn3 = BinaryTree(5)
btn1.left = btn2
btn1.right = btn3
# print_tree(btn1)
# print_tree_detailed(btn1)

r = take_input()
print_tree_detailed(r)
