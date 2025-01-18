"""
For a given binary tree of integers, find and return the sum of all the node data.
Sample Input:
    2 3 4 6 -1 -1 -1 -1  -1
Sample Output:
        15
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree_detailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data,end=" ")
    print()
    print_tree_detailed(root.left)
    print_tree_detailed(root.right)


def sum_nodes(root):
    if root is None:
        return 0
    x = root.data
    return x + sum_nodes(root.left) + sum_nodes(root.right)


btn1 = BinaryTree(2)
btn2 = BinaryTree(3)
btn3 = BinaryTree(4)
btn4 = BinaryTree(6)
btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
# print_tree_detailed(btn1)
print(sum_nodes(btn1))

