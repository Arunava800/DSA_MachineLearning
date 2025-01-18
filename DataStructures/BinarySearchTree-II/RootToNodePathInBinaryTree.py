"""
Given a data, find the node in the tree, return complete path from root to that
node.
Sample input: 1 2 3 -1 -1 4 6 5 -1 -1 9 7 8 -1 -1 -1 -1
k = 5
Output: [5, 4, 3, 1]
"""


import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print("enter the left child")
        left_data = int(input())
        if left_data != -1:
            left_child = BinaryTree(left_data)
            current.left = left_child
            q.put(left_child)
        print("enter the right child")
        right_data = int(input())
        if right_data != -1:
            right_child = BinaryTree(right_data)
            current.right = right_child
            q.put(right_child)
    return root


def node_to_root_path(root, s):
    if root is None:
        return None
    if root.data == s:
        returned_list = list()
        returned_list.append(root.data)
        return returned_list
    left_output = node_to_root_path(root.left, s)
    if left_output is not None:
        left_output.append(root.data)
        return left_output
    right_output = node_to_root_path(root.right, s)
    if right_output is not None:
        right_output.append(root.data)
        return right_output
    else:
        return None


tree_root = take_input()
x = int(input("Enter the values:"))
print(node_to_root_path(tree_root, x))
