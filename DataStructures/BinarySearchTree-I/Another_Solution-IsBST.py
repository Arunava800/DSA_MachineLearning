"""
Given a Binary tree, check if it is a BST or Not.
Time Complexity:
For a balanced tree, O(N)
For a skewed tree, O(N)
"""


import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    print("Enter the root: ")
    root_data = int(input())
    if root_data == -1:
        return None
    q = queue.Queue()
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("Enter the left child")
        root_left = int(input())
        if root_left != -1:
            left_child = BinaryTree(root_left)
            q.put(left_child)
            current.left = left_child
        print("Enter the right child")
        root_right = int(input())
        if root_right != -1:
            right_child = BinaryTree(root_right)
            q.put(right_child)
            current.right = right_child
    return root


def print_level_wise(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(current.data, end=":")
        if current.left is not None:
            left_child = current.left
            q.put(left_child)
            print("L:", left_child.data, end=",")
        if current.right is not None:
            right_child = current.right
            q.put(right_child)
            print("R:", right_child.data, end="")
        print()


def is_bst(root, min_range, max_range):
    if root is None:
        return True
    if root.data < min_range or root.data > max_range:
        return False
    is_left_constraint = is_bst(root.left, min_range, root.data - 1)
    is_right_constraint = is_bst(root.right, root.data, max_range)
    return is_left_constraint and is_right_constraint


root_tree = take_input()
print(is_bst(root_tree, -10000, 10000))
