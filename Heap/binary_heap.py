"""
Code for Heap data structure.
"""
class Heap:
    """
    A class to represent a heap.
    ...
    Attributes:
    ----------
    elements (List) : To store the elements of the heap

    Methods:
    -------
    insert() : To insert an element into the heap.
    delete() : To delete the root of the heap.
    is_empty() : Returns true if heap is empty, falses otherwise.
    """
    def __init__(self) -> None:
        self.elements = []

    def insert(self, data):
        """
        Method to insert an element into the heap.

        data (int) : Element to be inserted.
        """
        self.elements.append(data)
        temp = data
        i = len(self.elements) - 1

        while i > 0 and temp > self.elements[i//2]:
            self.elements[i] = self.elements[i//2]
            i //= 2

        self.elements[i] = temp

    def delete(self):
        """
        Method to delete the root of the heap.

        Returns: The root of the heap.
        """
        out = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()

        i = 0
        largest = 2*i + 1

        while largest < len(self.elements) - 1:
            if self.elements[largest] < self.elements[largest + 1]:
                largest += 1
            
            if self.elements[largest] > self.elements[i]:
                self.elements[largest], self.elements[i] = self.elements[i], self.elements[largest]
                i = largest
                largest = 2 * i
            else:
                break

        return out

    def is_empty(self):
        """
        Returns true if heap is empty, falses otherwise.
        """
        return len(self.elements) == 0

    def sort(self):
        new_heap = []
        for r in range(len(self.elements)):
            new_heap.append(self.delete())
        self.elements = new_heap
            
    def __str__(self) -> str:
        return " ".join([str(r) for r in self.elements])

b = Heap()
b.insert(50)
b.insert(30)
b.insert(20)
b.insert(15)
b.insert(10)
b.insert(8)
b.insert(16)
print(b)
b.insert(60)
b.sort()
print(b)