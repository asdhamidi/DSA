"""
Code for AVL Tree.
"""
from simple_tree import Tree
from binary_search_tree import inorder_predecessor, inorder_successor

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

    def _recursive_insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._recursive_insert(root.left, data)
        elif data > root.data:
            root.right = self._recursive_insert(root.right, data)

        root.height = self.max_height(root)

        return self.balanced(root)

    def delete(self, data):
        """
        Deletes the elemnent entered from the AVL tree.
        It balances the tree simultaneosuly.

        data (int): Key to be deleted.
        """
        self.root = self._delete(self.root, data)
    
    def _delete(self, root, data):
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
                temp = inorder_predecessor(root.left)
                root.data = temp.data
                root.left = self._delete(root.left, temp.data)
            else:
                temp = inorder_successor(root.right)
                root.data = temp.data
                root.right = self._delete(root.right, temp.data)

        root.height = self.max_height(root)
        return self.balanced(root)

    def max_height(self, root):
        """
        Returns the maxium height among subtree.
        
        root (Node): Node whose child Node's height are to be compared.
        
        returns (int): max of heights among left and right child Nodes.
        """
        return max(self.height(root.right), self.height(root.left))
    
    def balanced(self, root):
        """
        Balances the node after a delete or insert operation.
        
        root (Node): The node at which balance factor is checked and adjusted.

        returns : Node
        """
        if (self._balance_factor(root) == 2 and self._balance_factor(root.left) == 1):
            return self._LL_Rotation(root)
        if (self._balance_factor(root) == 2 and self._balance_factor(root.left) == -1):
            return self._LR_Rotation(root)
        if (self._balance_factor(root) == -2 and self._balance_factor(root.right) == -1):
            return self._RR_Rotation(root)
        if (self._balance_factor(root) == -2 and self._balance_factor(root.right) == 1):
            return self._RL_Rotation(root)

        return root

    ## Following functions help in doing rotations in the tree. 
    ## They are private as they are only used inside the class.
    def _LL_Rotation(self, root):
        rl = root.left
        rlr = rl.right

        rl.right = root
        root.left = rlr

        root.height = self.max_height(root)
        rl.height = self.max_height(rl)

        return rl

    def _LR_Rotation(self, root):
        pl = root.left
        plr = pl.right

        pl.right = plr.left
        root.left = plr.right

        plr.left = pl
        plr.right = root

        pl.height = self.max_height(pl)
        root.height = self.max_height(root)
        plr.height = self.max_height(plr)

        return plr

    def _RL_Rotation(self, root):
        pl = root.right
        plr = pl.left

        pl.left = plr.right
        root.right = plr.left

        plr.right = pl
        plr.left = root

        pl.height = self.max_height(pl)
        root.height = self.max_height(root)
        plr.height = self.max_height(plr)

        return plr

    def _RR_Rotation(self, root):
        rl = root.right
        rlr = rl.left

        rl.left = root
        root.right = rlr

        root.height = self.max_height(root)
        rl.height = self.max_height(rl)

        return rl

    def _balance_factor(self, root):
        return self.height(root.left) - self.height(root.right)