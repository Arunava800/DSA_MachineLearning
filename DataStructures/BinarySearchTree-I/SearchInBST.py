"""
Given a BST and an integer `k`. Find if the integer `k` is present in given BST or not.
You have to return True, if node with data `k` is present, return False otherwise. Assume
BST contains all unique elements.
Sample Input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1, 2
Sample Output: True
"""

import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    q = queue.Queue()
    print("Enter the root")
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left node")
        root_data_left = int(input())
        if root_data_left != -1:
            left_child = BinaryTree(root_data_left)
            current_node.left = left_child
            q.put(left_child)
        print("Enter the right side")
        root_data_right = int(input())
        if root_data_right != -1:
            right_child = BinaryTree(root_data_right)
            current_node.right = right_child
            q.put(right_child)
    return root


def print_level_wise(root):
    q = queue.Queue()
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=":")
        if current_node.left is not None:
            left_child = current_node.left
            q.put(left_child)
            print("L", left_child.data, end=",")
        if current_node.right is not None:
            right_child = current_node.right
            q.put(right_child)
            print("R", right_child.data, end="")
        print()


def search(root,x):
    if root is None:
        return False
    if root.data == x:
        return True
    elif root.data < x:
        return search(root.right, x)
    else:
        return search(root.left, x)


tree_root = take_input()
print_level_wise(tree_root)
k = int(input("Enter the element to be searched"))
print(search(tree_root, k))
