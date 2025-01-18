"""
Given a BST and an integer `k`, find and return the path from the node with data `k` and root
(if a node with data `k` is present in given BST) in a list. Return empty list otherwise.
Assume that BST contains all unique elements.
Sample Input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
k = 2
Sample Output: [2, 5, 8]
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
    q = queue.Queue()
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("enter the left child")
        left_root = int(input())
        if left_root != -1:
            left_child = BinaryTree(left_root)
            current.left = left_child
            q.put(left_child)
        print("enter the right child")
        right_root = int(input())
        if right_root != -1:
            right_child = BinaryTree(right_root)
            current.right = right_child
            q.put(right_child)
    return root


def path_in_bst(root, k):
    if root is None:
        return None
    if root.data == k:
        returned_list = list()
        returned_list.append(root.data)
        return returned_list
    if k < root.data:
        left_output = path_in_bst(root.left, k)
        if left_output is not None:
            left_output.append(root.data)
            return left_output
    else:
        right_output = path_in_bst(root.right, k)
        if right_output is not None:
            right_output.append(root.data)
            return right_output


root_tree = take_input()
print(path_in_bst(root_tree, 1))
