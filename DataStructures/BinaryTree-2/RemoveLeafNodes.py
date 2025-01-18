"""
For a given binary Tree, delete all the leaf nodes.
"""


from BinaryTree import take_input as tp, print_binary_tree as pb


def remove_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaf_nodes(root.left)
    root.right = remove_leaf_nodes(root.right)
    return root


r = tp()
pb(r)
remove_leaf_nodes(r)
