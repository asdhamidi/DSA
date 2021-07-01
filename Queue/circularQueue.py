import sys
sys.path.insert(0, 'C:/Users/asadu/Desktop/Code/DSA/Queue')
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

if __name__ == "__main__":
    q = CircularQueue()
    for r in range(5): q.enqueue(r)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(5)
    print(q)
    print("Size of the queue: ", q.length())
    for r in range(5): q.dequeue()
    print(q)

