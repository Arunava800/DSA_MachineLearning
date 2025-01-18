class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    root_data = int(input())
    if root_data == -1:
        return None
    tree_data = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    tree_data.left = left_tree
    tree_data.right = right_tree
    return tree_data


def print_binary_tree(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    print_binary_tree(root.left)
    print_binary_tree(root.right)
