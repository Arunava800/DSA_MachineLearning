"""
For a given binary tree of type integer, duplicate every node of the tree and attach it to
the left of itself. The root remains the same. So, you just need to insert the node in
the given binary tree
Sample Input:10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1
sample Output:
                                  10
                            10          30
                        20          30      60
                    20      50          60
                40      50
            40
"""

import queue
from sys import setrecursionlimit
setrecursionlimit(10**6)


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
            q.put(left_child)
            current.left = left_child
        print("enter the right child")
        right_data = int(input())
        if right_data != -1:
            right_child = BinaryTree(right_data)
            q.put(right_child)
            current.right = right_child
    return root


def insert_node(root):
    if root is None:
        return None

    insert_node(root.left)
    root_data = root.data
    node = BinaryTree(root_data)
    temp = root.left
    root.left, node.left = node, temp
    insert_node(root.right)
    return node


def print_level_wise(root):
    q = queue.Queue()
    print(root.data, end=":")
    q.put(root)
    while not q.empty():
        current = q.get()
        if current.left is not None:
            left_child = current.left
            print("L:", left_child.data, end=",")
            q.put(left_child)
        if current.right is not None:
            right_child = current.right
            print("R:", right_child.data, end="")
        print()


root_tree = take_input()
root_tree = insert_node(root_tree)
print_level_wise(root_tree)
