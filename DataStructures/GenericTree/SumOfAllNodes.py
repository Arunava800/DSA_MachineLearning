"""
Given a generic tree, find and return the sum of all the nodes present in the given tree.
Sample Input: 10 3 20 30 40 2 40 50 0 0 0 0
Sample output: 190
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def take_input():
    print("Enter the root: ")
    root_data = int(input())
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    print("Enter the number of children for ", root.data)
    child_count = int(input())
    for i in range(child_count):
        child = take_input()
        root.children.append(child)
    return root


def print_tree_detailed(root):
    if root is None:
        return None
    print(root.data,":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()
    for child in root.children:
        print_tree_detailed(child)


def print_sum(root):
    if root is None:
        return 0
    total = root.data
    for child in root.children:
        total = total +  print_sum(child)
    return total


new_root = take_input()
print(print_sum(new_root))