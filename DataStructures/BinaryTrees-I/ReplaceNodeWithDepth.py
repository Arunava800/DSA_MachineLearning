"""
For a given binary tree of integers, replace each of its data with the depth of the tree
Root is at depth 0, hence the root data is updated with 0. Replicate the same further going
down in the depth of the given tree. The modified tree will be printed in-order fashion.
Sample input:
  2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1
Sample output:
 2 1 2 0 2 1 2
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    root_data = int(input())
    if root_data == -1:
        return None
    tree = BinaryTree(root_data)
    left_tree = take_input()
    right_tree = take_input()
    tree.left = left_tree
    tree.right = right_tree
    return tree


def replace_nodes_depth(root, level = 0):

    if root is None:
        return 0
    root.data = level
    replace_nodes_depth(root.left, level+1)
    replace_nodes_depth(root.right, level+1)


