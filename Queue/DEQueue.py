import sys
sys.path.insert(0, 'C:/Users/asadu/Desktop/Code/DSA/Queue')
from simpleQueue import Queue, Node

class DEQueue(Queue):
    def enqueue_at_head(self, data):
        temp = self.front
        self.front = Node(data)
        self.front.next = temp
        self.len += 1
    
    def dequeue_at_rear(self):
        current = self.front
        while current.next.next:
            current = current.next

        print("Dequeued Elemnet :", current.next.data)
        self.rear = current
        self.rear.next = None
        self.len += 1

if __name__ == "__main__":
    q = DEQueue()
    for r in range(5): q.enqueue(r)
    print("Size of the queue: ", q.length())
    print("Middle Element: ", q.middle_element())
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(5)
    print(q)
    q.dequeue_at_rear()
    print(q)
    q.enqueue_at_head(9)
    print(q)

