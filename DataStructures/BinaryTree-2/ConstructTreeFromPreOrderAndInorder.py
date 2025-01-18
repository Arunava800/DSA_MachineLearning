"""
For a given preorder and inorder traversal of a binary tree of type integer stored in
array/list, create the binary tree using the given two arrays/list. You just need to
construct the tree and return the root.
Input: 1 2 4 5 3 6 7
        4 2 5 1 6 3 7
output: 1
    2           3
4       5   6       7
"""


import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(pre_order, in_order):
    index = -1
    if len(in_order) == 0:
        return None
    root_data = pre_order.pop(0)
    root_node = BinaryTree(root_data)
    for key, value in enumerate(in_order):
        if value == root_data:
            index = key
            break
    left_child = build_tree(pre_order,in_order[:index])
    right_child = build_tree(pre_order,in_order[index+1:])
    root_node.left = left_child
    root_node.right = right_child
    return root_node


def print_level_wise(root):
    q = queue.Queue()
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data,end=":")
        if current_node.left is not None:
            left_child = current_node.left
            q.put(left_child)
            print("L:", left_child.data, end=",")
        if current_node.left is None:
            print("L:",-1, end="")
        if current_node.right is not None:
            right_child = current_node.right
            q.put(right_child)
            print("R:", right_child.data, end="")
        if current_node.right is None:
            print("R:",-1, end="")
        print()




order_pre = [int(x) for x in input().split()]
order_in = [int(x) for x in input().split()]
root = build_tree(order_pre, order_in)
print_level_wise(root)
