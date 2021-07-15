"""
Code for a Binary Search Tree.
"""
from simple_tree import Tree, Node

class BST(Tree):
    """
    A class to represent a Tree.
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

    def recursive_insert(self, data):
        """
        Inserts an element into the Tree recursively.

        data (Any): Element to be inserted.
        """
        self.root = self._recursive_insert(self.root, data)

    def _recursive_insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._recursive_insert(root.left, data)
        elif data > root.data:
            root.right = self._recursive_insert(root.right, data)
        return root

    def delete(self, data):
        """
        Deletes the element if found in the tree.

        data (int): Element to be deleted.

        returns: None
        """
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        """
        Deletes the element if found in the tree.

        root(Node): Root of the tree.
        data (int): Element to be deleted.

        returns: Node
        """
        if root is None:
            return None

        if root.right is None and root.left is None:
            return None

        if data > root.data:
            root.right = self._delete(root.right, data)
        elif data < root.data:
            root.left =  self._delete(root.left, data)
        else:
            if self.height(root.left) > self.height(root.right):
                temp = self.inorder_predecessor(root.left)
                root.data = temp.data
                root.left = self._delete(root.left, temp.data)
            else:
                temp = self.inorder_successor(root.right)
                root.data = temp.data
                root.right = self._delete(root.right, temp.data)
        return root

    def _inverse(self, root):
        if root.left is None and root.right is None:
            return root

        root.left, root.right = root.right, root.left

        root.left = self._inverse(root.left)
        root.right = self._inverse(root.right)

        return root

    def inverse(self):
        """
        Inverses a Binary Search Tree.
        """
        self.root = self._inverse(self.get_root())

    def get_largest(self, root):
        l = r = 0

        if root.left: l = self.get_largest(root.left)
        if root.right: r = self.get_largest(root.right)

        return max(root.data, max(l, r))

    def get_smallest(self, root):
        l = r = float("inf")

        if root.left: l = self.get_smallest(root.left)
        if root.right: r = self.get_smallest(root.right)

        return min(root.data, min(l, r))
    
    def total_nodes(self, root):
        if not root:
            return 0
        
        l = self.total_nodes(root.left)
        r = self.total_nodes(root.right)
        
        return l + r + 1
    
    def total_leaf_nodes(self, root):
        if root is None:
            return 0 
            
        if root.left is None and root.right is None:
            return 1
        
        l = self.total_leaf_nodes(root.left)
        r = self.total_leaf_nodes(root.right)
        
        return l + r

    def only_left(self, root):
        if not root:
            return 0
        
        if root.right is None and root.left is not None:
            return self.only_left(root.left) + 1
        else:
            l = self.only_left(root.left)
            r = self.only_left(root.right)

            return l + r
    
    def only_right(self, root):
        if not root:
            return 0
        
        if root.right is not None and root.left is None:
            return self.only_right(root.right) + 1
        else:
            l = self.only_right(root.left)
            r = self.only_right(root.right)

            return l + r
            
    @staticmethod
    def inorder_successor(root):
        """
        Returns inorder successor.

        root(Node): Right the child of the Node.
        """
        while root and root.left:
            root = root.left
        return root

    @staticmethod
    def inorder_predecessor(root):
        """
        Returns inorder predecessor.

        root(Node): Left the child of the Node.
        """
        while root and root.right:
            root = root.right
        return root


b = BST()
b.insert(7)
b.insert(2)
b.insert(4)
b.insert(1)
b.insert(6)
b.insert(8)
b.insert(9)

print(b.get_largest(b.get_root()))
print(b.get_smallest(b.get_root()))
print(b.total_nodes(b.get_root()))
print(b.total_leaf_nodes(b.get_root()))
print(b.only_left(b.get_root()))
print(b.only_right(b.get_root()))