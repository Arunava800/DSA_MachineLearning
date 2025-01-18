"""
Given a generic tree,
"""
import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def take_input():
    q = queue.Queue()
    print("Enter the root: ")
    root_data = int(input())
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("How many children for ", current.data)
        count_child = int(input())
        for i in range(count_child):
            print("Enter the next child")
            child_data = int(input())
            child = TreeNode(child_data)
            current.children.append(child)
            q.put(child)
    return root


def print_level_wise(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(current.data, ":", end="")
        for child in current.children:
            print(child.data, end=",")
            q.put(child)
        print()


def count_height(root):
    if root is None:
        return 0
    count = 0
    for i in range(len(root.children)):
        count = max(count, count_height(root.children[i]))
    return count + 1


root_wise = take_input()
print_level_wise(root_wise)
print(count_height(root_wise))