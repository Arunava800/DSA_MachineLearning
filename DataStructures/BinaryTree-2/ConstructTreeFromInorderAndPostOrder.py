"""
For a given post-order and in-order traversal of a Binary Tree of type integer stored in
an array/list, create the binary tree using the given two array/lists. You just need to
construct the tree and return the root.

Assume that the binary tree also contains only the unique elements
Sample Input:
    post-order: 4 5 2 6 7 3 1
    in-order: 4 2 5 1 6 3 7
Sample Output
                1
            2           3
        4       5   6       7
"""

import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(post, ino):
    if len(ino) == 0 or len(post) == 0:
        return None
    root_index = -1
    root_data = post.pop()
    for key, value in enumerate(ino):
        if value == root_data:
            root_index = key
            break
    root = BinaryTree(root_data)
    right_child = build_tree(post, ino[root_index + 1:])
    left_child = build_tree(post, ino[:root_index])

    root.left = left_child
    root.right = right_child
    return root


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


post_order = [int(x) for x in input().split()]
in_order = [int(x) for x in input().split()]
tree = build_tree(post_order, in_order)
print_level_wise(tree)
