"""
Create a generic tree.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def print_tree(root):
    if root is None:
        return
    print(root.data, end=" ")
    for child in root.children:
        print_tree(child)


def print_tree_detailed(root):
    if root is None:
        return
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data,",",end="")

    print()
    for child in root.children:
        print_tree_detailed(child)


n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(7)
n6 = TreeNode(15)
n7 = TreeNode(1)
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)
n3.children.append(n6)
n3.children.append(n7)
print_tree(n1)
print()
print_tree_detailed(n1)
