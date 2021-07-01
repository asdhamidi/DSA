"""
Code for a Node object and a Tree object.
"""
import sys
sys.path.append('C:/Users/asadu/Desktop/Code/DSA/Queue')
from simpleQueue import Queue

class Node(object):
    """
    A class to represent node for graphs and Trees.
    ...

    Attributes:
    ----------
    data : str, int
        Data for the node
    right : Node
        Points to the right child Node.
    left : Node
        Points to the left child Node.
    """
    def __init__(self, data) -> None:
        """
        @params:
        data : int, str
            Data for the Node.
        """
        self.data = data
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return str(self.data)

class Tree():
    """
    A class to reresent a Tree.
    ...
    Attributes:
    ----------
    root : Node
        Points to the root Node.

    Methods:
    -------
    create()
        Method to create a tree using queue.
    get_height()
        Method to find the height of the Tree.
    show()
        Method for displaying the tree.
    """
    def __init__(self) -> None:
        self.root = None

    def create(self):
        """
        Method for creating the Tree.
        Uses a Queue data structure to implement a Tree through Inorder.
        
        returns : None
        """
        q = Queue()
        self.root = Node(input("Enter the root value: "))
        q.enqueue(self.root)

        while(not q.is_empty()):
            p = q.dequeue()
            l = int(input("Enter left child of {}: ".format(p.data)))
            if (l != -1):
                left = Node(l)
                p.data.left = left
                q.enqueue(left)

            r = int(input("Enter right child {}: ".format(p.data)))
            if (r != -1):
                right = Node(r)
                p.data.right = right
                q.enqueue(right)
    
    def get_root(self):
        return self.root

    def height(self, root):
        """
        Returns the height of the tree.
        
        root (Node): Base of the tree.

        returns : int - height of the tree
        """
        if not root:
            return 0

        l = self.height(root.left)
        r = self.height(root.right)

        return l + 1 if l > r else r + 1

    def _preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data, end=" ")

    def _levelorder(self, root):
        q = Queue()
        q.enqueue(root)
        while(not q.is_empty()):
            p = q.dequeue()
            print(p.data.data)
            if p.data.left: q.enqueue(p.data.left)
            if p.data.right: q.enqueue(p.data.right)

    def count(self, root):
        """
        Returns number of nodes in a Tree.

        root (Node): Base of the tree.

        returns: int - number of nodes in a Tree.
 
        """
        if root:
            return self.count(root.left) + self.count(root.right) + 1
        return 0

    def show(self, type=1):
        """
        Method to print the Tree in preorder, inorder, and postorder traversal.
        
        type (int): Type of traversal required.
                    1. Preorder
                    2. Inorder
                    3. Postorder
                    4. Levelorder
        """
        if type == 1:
            self._preorder(self.root)
        elif type == 2:
            self._inorder(self.root)
        elif type == 3:
            self._postorder(self.root)
        else:
            self._levelorder(self.root)