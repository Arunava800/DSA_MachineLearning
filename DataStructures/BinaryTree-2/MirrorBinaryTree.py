"""
For a given binary tree, update it with its corresponding mirror image.
    1                                   1
  2    3    ===============>        3       2
 4 5  6  7                         7 6     5  4
"""

from BinaryTree import take_input as tp, print_binary_tree as pb


def mirror_binary_tree(root):
    if root is None:
        return
    if root.left is not None and root.right is not None:
        root.left, root.right = root.right, root.left
    if root.left is None and root.right is not None:
        root.left, root.right= root.right, root.left
    if root.right is None and root.left is not None:
        root.right, root.left = root.left, root.right
    mirror_binary_tree(root.left)
    mirror_binary_tree(root.right)

    return root


r = tp()
r = mirror_binary_tree(r)
pb(r)