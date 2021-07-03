"""
Code for AVL Tree.
"""
from simple_tree import Tree

class Node():
    """
    Class to represent Node object for an AVL tree.

    Attributes:
    ----------
    data (int): data of the Node
    left (Node): points to the left child
    right (Node): points to the right child

    Methods:
    -------
    get_data(): returns the data
    get_height(): returns the height of the Node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_data(self) -> int:
        """
        Returns self.data
        """
        return self.data

    def get_height(self) -> int:
        """
        Returns self.height
        """
        return self.height

class AVL(Tree):
    """
    Class to represent AVL Tree.

    Methods:
    -------
    recursive_insert(data): Method to insert an element recursively.
    """
    def recursive_insert(self, data):
        """
        Method to insert an element recursively.

        data (int): Data to be entered into the new element.
        """
        self.root = self._recursive_insert(self.root, data)

    def _LL_Rotation(self, root):
        rl = root.left
        rlr = rl.right

        rl.right = root
        root.left = rlr

        root.height = max(self.height(root.right), self.height(root.left))
        rl.height = max(self.height(rl.right), self.height(rl.left))

        return rl

    def _LR_Rotation(self, root):
        pass

    def _RL_Rotation(self, root):
        pass

    def _RR_Rotation(self, root):
        pass

    def _balance_factor(self, root):
        return self.height(root.left) - self.height(root.right)

    def _recursive_insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._recursive_insert(root.left, data)
        elif data > root.data:
            root.right = self._recursive_insert(root.right, data)

        root.height = max(self.height(root.right), self.height(root.left))

        if (self._balance_factor(root) == 2 and self._balance_factor(root.left) == 1):
            return self._LL_Rotation(root)
        if (self._balance_factor(root) == 2 and self._balance_factor(root.left) == -1):
            return self._LR_Rotation(root)
        if (self._balance_factor(root) == -2 and self._balance_factor(root.right) == -1):
            return self._RR_Rotation(root)
        if (self._balance_factor(root) == -2 and self._balance_factor(root.right) == 1):
            return self._RL_Rotation(root)

        return root
