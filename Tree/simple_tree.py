"""
Code for a Node object and a Tree object.
"""
import sys
sys.path.append('C:/Users/asadu/Desktop/Code/DSA/Queue')
from simpleQueue import Queue

class Node():
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

    def get_data(self):
        """
        Returns self.data.
        """
        return self.data
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
    count()
        Method to count number of nodes in the tree.
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
        queue = Queue()
        self.root = Node(input("Enter the root value: "))
        queue.enqueue(self.root)

        while not queue.is_empty():
            current = queue.dequeue()
            lchild = int(input("Enter left child of {}: ".format(current.data)))
            if lchild != -1:
                left = Node(lchild)
                current.data.left = left
                queue.enqueue(left)

            rchild = int(input("Enter right child {}: ".format(current.data)))
            if rchild != -1:
                right = Node(rchild)
                current.data.right = right
                queue.enqueue(right)

    def get_root(self):
        """
        Returns self.root
        """
        return self.root

    def height(self, root):
        """
        Returns the height of the tree.

        root (Node): Base of the tree.

        returns : int - height of the tree
        """
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return left + 1 if left > right else right + 1

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

    def _levelorder(self):
        root = self.get_root()
        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            current = queue.dequeue()
            print(current.data.data)
            if current.data.left:
                queue.enqueue(current.data.left)
            if current.data.right:
                queue.enqueue(current.data.right)

    def count(self, root):
        """
        Returns number of nodes in a Tree.

        root (Node): Base of the tree.

        returns: int - number of nodes in a Tree.

        """
        if root:
            return self.count(root.left) + self.count(root.right) + 1
        return 0

    def show(self, order=1):
        """
        Method to print the Tree in preorder, inorder, and postorder traversal.

        order (int): Type of traversal required.
                    1. Preorder
                    2. Inorder
                    3. Postorder
                    4. Levelorder
        """
        if order == 1:
            self._preorder(self.root)
        elif order == 2:
            self._inorder(self.root)
        elif order == 3:
            self._postorder(self.root)
        elif order == 4:
            self._levelorder()
        else:
            return
