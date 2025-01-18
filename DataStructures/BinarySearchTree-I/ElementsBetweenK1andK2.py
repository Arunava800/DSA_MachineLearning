"""
Given a binary search tree and two integers, k1 and k2, find and print the elements which are
in range of k1 and k2 (both inclusive).
Sample input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
k1:6 , k2: 10
Sample output: 6 7 8 10(not ascending order)
"""


import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    q = queue.Queue()
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("Enter the left")
        root_left = int(input())
        if root_left != -1:
            left_child = BinaryTree(root_left)
            q.put(left_child)
            current.left = left_child
        print("Enter the right")
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
            print("L", left_child.data, end=",")
            q.put(left_child)
        if current.right is not None:
            right_child = current.right
            print("R", right_child.data, end=",")
            q.put(right_child)
        print()


def elements_between_range(root, k1, k2):
    if root is None:
        return None
    if root.data > k2:
        elements_between_range(root.left, k1, k2)
    elif root.data < k1:
        elements_between_range(root.right, k1, k2)
    elif k1 <= root.data <= k2:
        print(root.data, end="")
    else:
        elements_between_range(root.left, k1, k2)
        elements_between_range(root.right, k1, k2)


root_tree = take_input()
print_level_wise(root_tree)
element_1 = int(input("Enter value for k1"))
element_2 = int(input("Enter value for k2"))
elements_between_range(root_tree, element_1, element_2)
