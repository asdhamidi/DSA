"""
Code for stack data structure.
"""
import sys
sys.path.append("../DSA/LL")
from linked_list import Node

class Stack:
    """
    A class to represent a heap.
    ...
    Attributes:
    ----------
    head (Node) : Stores the head of the stack.

    Methods:
    -------
    push() : To insert an element into the stack.
    pop() : To remove the head of the heap.
    peek() : Returns the head of the stack.
    """
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        """
        Method to insert an element into the stack.

        data (int) : Element to be inserted.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        Method to delete the root of the stack.

        Returns: The root of the stack.
        """
        if self.head:
            out = self.head
            self.head = self.head.next
            return out.data
        raise Exception("Underflow")

    def peek(self):
        """
        Returns the head of the stack.
        """
        return self.head.data

    def __str__(self) -> str:
        out = ""
        current = self.head
        while current:
            out += str(current.data) + " "
            current = current.next

        return out
