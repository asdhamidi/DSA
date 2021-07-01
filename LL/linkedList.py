class Node:
    """
    Object Node
    """
    def __init__(self, data):
        """
        Constructor functions
        @params : data
        """
        self.data = data
        self.next = None
    def get_data(self):
        """
        Getter function
        @returns : data
        """
        return self.data

class LinkedList:
    """
    Object type : Linked List
    """
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head= Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.get_data(), end="->")
            current = current.next

    def display_reverse(self, head):
        if head != None:
            self.display_reverse(head.next)
        else:
            return
        print(head.getData(),end="->")

    def delete(self, data):
        if self.head == None:
            print("Empty List")
            return


        if self.head.getData() == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next.data != data:
            current = current.next

        if current == None:
            print("Element Not found")
        else:
            current.next = current.next.next

    def deleteRecursive(self, head, data):
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

        self.deleteRecursive(prev.next, data)

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_recursive(self, head):
        if head is None or head.next is None:
            return head

        rest = self.reverse_recursive(head.next)

        head.next.next = head
        head.next = None

        return rest

    def get_middle_element(self):
        head = head1 = self.getHead()
        while head1 != None and head1.next != None:
            head1 = head1.next.next
            head = head.next

        print("Middle Element : ", head.data)

if __name__ == "__main__":
    q = LinkedList()
    for r in range(1, 6):
        q.insert(r)
    print("Before reversing : ",end="")
    q.display()
    print()
    q.head = q.reverse_recursive(q.getHead())
    print("After Reversing : ",end="")
    q.display()
    print()
    q.get_middle_element()
