import sys
sys.path.insert(0, 'C:/Users/asadu/Desktop/Code/DSA/Queue')
from simpleQueue import Queue, Node

class PriorityQueue(Queue):
    def dequeue(self):
        current = self.front.next
        max = self.front.data
        while current:
            if max < current.data:
                max = current.data
            current = current.next
        
        if max == self.front.data:
            self.front = self.front.next
        else:
            current = self.front
            while current.next.data != max:
                current = current.next
            current.next = current.next.next
            self.len -= 1

if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(9)
    q.enqueue(3)
    print(q)
    print("Size of the queue: ", q.length())
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    print("Size of the queue: ", q.length())
