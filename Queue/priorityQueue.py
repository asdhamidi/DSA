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
