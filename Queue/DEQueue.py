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

