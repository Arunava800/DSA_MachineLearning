"""
Implement the BST class which includes the following:
1. insert - Given an element, insert that  element in the BST at the correct position. if
the element is equal to the data of the node, insert it in the left subtree
2. search - Given an element, find if that is present in BST or not. Return true or false.
3. delete - Given an element, remove that element from the BST. If the element which is to
be deleted has both children, replace that with a minimum element from right-subtree.
4. printTree() - print the BST in the following format. For printing a node N, you need the
exact format -
    N:L:x,R:y
where N is the data at any node in the binary tree. x and y are the values of the left
and right child of node N. Print the children only if it is not null.
There is no space in between. You need to print all nodes in the recursive format in
different lines.
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def print_tree_helper(self, root):
        if root is None:
            return None
        print(root.data, end=":")
        if root.left is not None:
            print("L:", root.left.data, end=",")
        if root.right is not None:
            print("R:", root.right.data)
        self.print_tree_helper(root.left)
        self.print_tree_helper(root.right)
        print()

    def print_tree(self):
        self.print_tree_helper(self.root)

    def insert_helper(self, root, data):
        if root is None:
            node = BinaryTree(data)
            return node
        if data <= root.data:
            root.left = self.insert_helper(root.left, data)
            return root
        else:
            root.right = self.insert_helper(root.right, data)
            return root

    def search_helper(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            self.search_helper(root.left, data)
        else:
            self.search_helper(root.right, data)

    def search(self, data):
        return self.search_helper(self.root, data)

    def minimum(self, root):
        if root is None:
            return 10000
        if root.left is None:
            return root.data
        return self.minimum(root.left)

    def delete_helper(self, root, data):
        if root is None:
            return False, None
        if root.data < data:
            deleted, new_right_node = self.delete_helper(root.right, data)
            root = new_right_node
            return deleted, root
        if root.data > data:
            deleted, new_left_node = self.delete_helper(root.left, data)
            root = new_left_node
            return deleted, root
        if root.left is None and root.right is None:
            return True, None
        if root.left is None:
            return True, root.right
        if root.right is None:
            return True, root.left
        replacement = self.minimum(root.right)
        root.data = replacement
        deleted, new_right_node = self.delete_helper(root.right, replacement)
        root.right = new_right_node
        return True, root

    def delete(self, data):
        deleted, new_root = self.delete_helper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = new_root
        return deleted

    def insert(self, data):
        self.root = self.insert_helper(self.root, data)
        self.numNodes += 1
        return self.root


bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.print_tree()
# element = int(input("Enter the element to be searched"))
# bst.search(element)
element = int(input("enter the element to be deleted"))
print(bst.delete(element))
bst.print_tree()