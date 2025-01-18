"""
Take input defined by the user
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
    print("Enter the number of children for ", root_data)
    child_count = int(input())
    for i in range(child_count):
        child = take_input()
        root.children.append(child)
    return root


def print_tree_detailed(root):
    if root is None:  # not a base case but an edge case
        return None
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()
    for child in root.children:
        print_tree_detailed(child)


new_root = take_input()
print_tree_detailed(new_root)
