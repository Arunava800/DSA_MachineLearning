"""
Find the total number of nodes present in a generic tree.
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
    print("How many children does the", root.data, "have? ")
    child_count = int(input())
    for i in range(child_count):
        child = take_input()
        root.children.append(child)
    return root


def print_root_detailed(root):
    if root is None:
        return None
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    for child in root.children:
        print_root_detailed(child)


def count_nodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count = count + count_nodes(child)
    return count


new_root = take_input()
count_nodes(new_root)