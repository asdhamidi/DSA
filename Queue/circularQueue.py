from simpleQueue import Queue, Node

class CircularQueue(Queue):
    def enqueue(self, data):
        if self.front == None:
            self.front = self.rear = Node(data)
            self.rear.next = self.front
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
            self.rear.next = self.front
        self.len += 1
    
    def dequeue(self):
        if self.front == None:
            print("Underflow. \nQueue is Empty.")
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            print("Dequeued element: ", self.front.data)
            self.front = self.front.next
            self.rear.next = self.front
            self.len -= 1
    
    def __str__(self) -> str:
        if not self.front:
            return "Queue is Empty."
        else:
            current = self.front
            s = ""
            while current.next != self.front:
                s += (str(current.data)+"->")
                current = current.next
            s += str(current.data)
            return s
