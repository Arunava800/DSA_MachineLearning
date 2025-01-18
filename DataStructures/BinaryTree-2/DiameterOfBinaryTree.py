"""
For a given binary of type integer, find and return the `Diameter`.
The diameter of the tree can be defined as the maximum distance between two leaf nodes. Here,
the distance is measured in terms of the total number of nodes present along the path of the
two leaf nodes, including both the leaves.
Input:
                    2
                4       5
            6               7
        20      30      80      90
              8             9
Output: The total distance is 9, both 8 and 9 nodes inclusive
"""


from BinaryTree import take_input


def height_and_diameter(root):
    if root is None:
        return 0,0
    left_height, left_diameter = height_and_diameter(root.left)
    right_height, right_diameter = height_and_diameter(root.right)
    current_height = 1 + max(left_height, right_height)
    current_diameter = max(left_height+right_height+1, left_diameter, right_diameter)
    return current_height, current_diameter


def diameter_binary_tree(root):
    _, diameter = height_and_diameter(root)
    return diameter


elements = take_input()
print(diameter_binary_tree(elements))
