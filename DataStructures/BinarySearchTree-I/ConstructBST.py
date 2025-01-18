"""
Given a sorted integer array A of size `n`, which contains all unique elements. You need to
construct a balanced BST tree from this input array. Return the root of the constructed BST.
If array size is even take first mid as the root
Sample Input: 1 2 3 4 5 6 7
Output: 4 2 1 3 6 5 7
"""

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


def construct_bst(array):
    if len(array) == 0:
        return None
    mid = len(array) // 2
    if len(array) % 2 == 0:
        mid = mid - 1
    root = BinaryTree(array[mid])
    left_child = construct_bst(array[:mid])
    right_child = construct_bst(array[mid+1:])
    root.left = left_child
    root.right = right_child
    return root


def pre_order(root):
    if root is None:
        return None
    print(root.data, end='')
    pre_order(root.left)
    pre_order(root.right)


elements = [int(x) for x in input().split()]
root_tree = construct_bst(elements)
# print_level_wise(root_tree)
pre_order(root_tree)


