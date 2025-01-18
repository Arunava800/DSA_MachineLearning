"""
Given a binary tree, check if the tree is balanced or not, i.e, for each node in a tree,
the node's left and right subtree should not have a height difference more than 1.
"""

from BinaryTree import take_input


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    is_balanced_left = is_balanced(root.left)
    is_balanced_right = is_balanced(root.right)
    if is_balanced_left and is_balanced_right:
        return True
    else:
        return False


r = take_input()
print(is_balanced(r))