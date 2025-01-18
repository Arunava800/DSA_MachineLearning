"""
____________________________FIND THE LARGEST NODE________________________________________
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
    root_tree = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    root_tree.left = left_tree
    root_tree.right = right_tree
    return root_tree


def largest_data(root):
    if root is None:
        return -1
    left_largest = largest_data(root.left)
    right_largest = largest_data(root.right)
    largest = max(left_largest, right_largest, root.data)
    return largest


r = take_input()
print(largest_data(r))