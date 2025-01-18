"""
Given a Binary tree, check if it is a BST or Not.
Time Complexity:
For a balanced tree, O(NlogN)
For a skewed tree, O(N^2)
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


def min_tree(root):
    if root is None:
        return 10000
    left_min = min_tree(root.left)
    right_min = min_tree(root.right)
    minimum = min(left_min, right_min, root.data)
    return minimum


def max_tree(root):
    if root is None:
        return -10000
    left_max = max_tree(root.left)
    right_max = max_tree(root.right)
    return max(left_max, right_max, root.data)


def is_bst(root):
    if root is None:
        return True
    left_max = max_tree(root.left)
    right_min = min_tree(root.right)
    if root.data > right_min or root.data <= left_max:
        return False
    is_left_bst = is_bst(root.left)
    is_right_bst = is_bst(root.right)
    return is_left_bst and is_right_bst


root_tree = take_input()
print_level_wise(root_tree)
print(is_bst(root_tree))
