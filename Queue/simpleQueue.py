"""
Code for a simple queue data structure.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self, data):
        if self.front == None:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        self.len += 1
    
    def dequeue(self):
        if self.front == None:
            print("Underflow. \nQueue is Empty.")
        else:
            removed = self.front
            self.front = self.front.next
            self.len -= 1
            return removed
    
    def is_empty(self):
        return self.len == 0
    
    def __str__(self) -> str:
        if not self.front:
            return "Queue is Empty."
        else:
            current = self.front
            s = ""
            while current:
                s += (str(current.data)+"->")
                current = current.next
            return s
    
    def middle_element(self):
        start1 = start2 = self.front
        while start2 and start2.next:
            start1 = start1.next
            start2 = start2.next.next
        return start1.data
    
    def length(self):
        return self.len
