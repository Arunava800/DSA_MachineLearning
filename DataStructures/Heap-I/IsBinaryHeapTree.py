"""
You have been given a binary tree of integers. Your task is to check whether binary heap tree or not.
A binary tree is at ree in which each parent node has at most two children.
A binary heap tree has the following properties:
1. It must be a complete binary tree. In the complete binary tree, every level, except the last level is completely
filled and the last level is as far left as possible.
2. Every parent must be greater than all its children node.
"""


is_heap = True


def is_leaf(node) -> bool:
    if not node.left and not node.right:
        return True
    return False


def check(node) -> int:
    global is_heap
    if is_leaf(node):
        return node.data
    if not node.left:
        is_heap = False
        return node.data
    if node.left and not node.right and not is_leaf(node.left):
        is_heap = False
        return node.data
    max_left = check(node.left)
    max_right = check(node.right)
    if node.right:
        max_right = check(node.right)
    maximum = max(max_left, max_right)
    if maximum == node.data:
        return node.data
    else:
        is_heap = False
        return maximum


def is_binary_heap_tree(root):
    global is_heap
    is_heap = True
    check(root)
    return is_heap
