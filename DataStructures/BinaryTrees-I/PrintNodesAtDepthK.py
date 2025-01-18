"""
Print the nodes at depth K
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


# Method 1
def print_depth_k(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    print_depth_k(root.left, k-1)
    print_depth_k(root.right, k-1)


# Method 2
def print_depth_d(root, k, d =0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    print_depth_d(root.left, k, d+1)
    print_depth_d(root.right, k, d+1)
