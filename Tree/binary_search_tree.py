"""
Code for a Binary Search Tree.
"""
from simple_tree import Tree, Node

class BST(Tree):
    """
    A class to reresent a Tree.
    ...
    Attributes:
    ----------
    root : Node
        Points to the root Node.

    Methods:
    -------
    search(root, data):
        Method to search for an element in the tree.
    insert(data):
        Method to insert an element into the tree.
    """
    def search(self, root, data):
        """
        Method for searching for an element in a BST.

        root (Node): Base of the tree.
        data (int/str): Element to look for in the tree.

        returns: True if element is found, False otherwise.
        """
        if not root: # Base Case
            return False

        if data == root.data:
            return True
        if data > root.data:
            return self.search(root.right, data)
        if data < root.data:
            return self.search(root.left, data)

    def insert(self, data):
        """
        Method for inserting an element in a BST.

        root (Node): Base of the tree.
        data (int/str): Element to look for in the tree.

        returns: None
        """
        if not self.root:
            self.root =  Node(data)
        else:
            root = self.root
            while root:
                if root.data == data:
                    return
                if data > root.data:
                    if root.right:
                        root = root.right
                    else:
                        root.right = Node(data)
                        return
                else:
                    if root.left:
                        root = root.left
                    else:
                        root.left = Node(data)
                        return

    def delete(self, data):
        """
        Deletes the element if found in the tree.

        data (int): Element to be deleted.

        returns: None
        """
