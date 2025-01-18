import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_level_wise_input():
    q = queue.Queue()
    print("Enter the root")
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left child")
        left_child_data = int(input())
        if left_child_data != -1:
            left_child = BinaryTree(left_child_data)
            current_node.left = left_child
            q.put(left_child)
        print("Enter the right child")
        right_child_data = int(input())
        if right_child_data != -1:
            right_child = BinaryTree(right_child_data)
            current_node.right = right_child
            q.put(right_child)
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
            print("L:",-1)
        if current_node.right is not None:
            right_child = current_node.right
            q.put(right_child)
            print("R:", right_child.data, end="")
        if current_node.right is None:
            print("R:",-1)
        print()


root_tree = take_level_wise_input()
print_level_wise(root_tree)