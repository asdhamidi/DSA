
class Node:
    def __init__(self,data: Any) -> None:
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data: Any):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next
            
            temp.next = new_node
            new_node.next = self.head
    
    def delete(self, data):
        if self.head is None:
            print("Empty List")
        elif data == self.head.data and self.head.next == self.head:
            self.head = None
        elif data == self.head.data:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            
            temp.next = self.head.next
            self.head = self.head.next
        else:
            temp = self.head

            while temp.next.data != data and temp.next != self.head:
                temp = temp.next

            if temp.next == self.head:
                print("Element Not In The List")
            else:
                temp.next = temp.next.next
        
    def __str__(self) -> str:
        if self.head is None:
            return "Empty List"
        else:
            s = ""
            temp = self.head
            while temp.next != self.head:
                s += str(temp.data)
                temp = temp.next
            s += str(temp.data)
            return s
