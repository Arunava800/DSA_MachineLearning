"""
Given a generic tree, find and return the node maximum data. You need to return the node
which is having maximum data.
Return null if tree is empty.
Sample Input: 10 3 20 30 40 2 40 50 0 0 0 0
Sample Output: 50

"""


class NodeTree:
    def __init__(self, data):
        self.data = data
        self.children = list()


def take_input():
    print("Enter the root node")
    root_data = int(input())
    if root_data == -1:
        return None
    root = NodeTree(root_data)
    print("Enter the children for", root.data)
    child_count = int(input())
    for i in range(child_count):
        child_root = take_input()
        root.children.append(child_root)
    return root


def print_root_detailed(root):
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    for child in root.children:
        print_root_detailed(child)


def max_helper(curr_node, max_node):
    if curr_node is None:
        return None
    if max_node.data < curr_node.data:
        max_node = curr_node
    for i in range(len(curr_node.children)):
        max_helper(curr_node.children[i], max_node)
    return max_node


def max_data(root):
    ans = root
    max_helper(root, ans)
    return ans


new_root = take_input()
print(max_data(new_root).data)
