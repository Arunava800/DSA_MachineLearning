"""
For a given binary tree of type integers, print all the nodes without any siblings.
Example Input:
1  4 5 6 -1 -1 7 20 30 80 90 -1 -1 -1 -1 -1 -1 -1 -1
Example output: 6 7

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


def print_node_without_siblings(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data, end=" ")

    if root.left is None and root.right is not None:
        print(root.right.data, end=" ")

    print_node_without_siblings(root.left)
    print_node_without_siblings(root.right)


r = take_input()
print_node_without_siblings(r)