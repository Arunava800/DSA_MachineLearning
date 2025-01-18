import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def take_input_level_wise():
    q = queue.Queue()
    print("Enter the root: ")
    root_data = int(input())
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("Enter the number of children for", current.data)
        num_child = int(input())
        for i in range(num_child):
            print("Enter the next_child", root.data)
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


new_root = take_input_level_wise()
print_level_wise(new_root)