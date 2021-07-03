"""
Code for Linked List.
"""
class Node:
    """
    Object Node
    ...
    Attributes:
    ----------
    data (int) : data for the node
    next (Node) : Points to the next node

    Methods:
    -------
    get_data(): returns data of the node
    """
    def __init__(self, data):
        """
        Constructor function
        parameters:
        data (int) : data for the node.
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Getter function for self.data
        """
        return self.data

class LinkedList:
    """
    Object type : Linked List
    ...
    Attributes:
    ----------
    head (Node): Head of the LL.

    Methods:
    -------
    get_head(): returns self.head
    insert(data): inserts an element in the LL.
    display(): displays the LL.
    display_reverse(): displays the LL in reverse.
    delete(data)/delete_recursive(head, data):
        deletes an element in the LL, if found.
    reverse()/reverse_recursive(): reverses the LL.
    get_middle_element(): returns the middle element.
    """
    def __init__(self):
        self.head = None

    def get_head(self):
        """
        Returns self.head
        """
        return self.head

    def insert(self, data):
        """
        Inserts a element in the LL.

        data(int): element to be inserted.
        """
        if not self.head:
            self.head= Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def display(self):
        """
        Displays the list.
        """
        current = self.head
        while current:
            print(current.get_data(), end="->")
            current = current.next

    def display_reverse(self, head):
        """
        Displays the LL in reverse.

        head(Node): head of the LL.
        """
        if head is not None:
            self.display_reverse(head.next)
        else:
            return
        print(head.getData(),end="->")

    def delete(self, data):
        """
        Deletes an element from the LL.

        data(int): element to be deleted.
        """
        if self.head is None:
            print("Empty List")
            return


        if self.head.getData() == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next.data != data:
            current = current.next

        if current is None:
            print("Element Not found")
        else:
            current.next = current.next.next

    def delete_recursive(self, head, data):
        """
        Deletes an element from the LL.

        head(Node): head of the LL.
        data(int): element to be deleted.
        """
        if head is None:
            print("Element Not Found")
            return

        if head == self.head:
            if data == head.getData():
                self.head = self.head.next
                return

        prev = head
        head = head.next
        if head is not None:
            if head.getData() == data:
                prev.next = head.next
                return

        self.delete_recursive(prev.next, data)

    def reverse(self):
        """
        Reverses the LL.
        """
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_recursive(self, head):
        """
        Reverses the LL recursively.

        head (Node): Head of the LL.
        """
        if head is None or head.next is None:
            return head

        rest = self.reverse_recursive(head.next)

        head.next.next = head
        head.next = None

        return rest

    def get_middle_element(self):
        """
        Returns the middle element of the LL.
        """
        head = head1 = self.get_head()
        while head1 is not None and head1.next is not None:
            head1 = head1.next.next
            head = head.next

        print("Middle Element : ", head.data)
