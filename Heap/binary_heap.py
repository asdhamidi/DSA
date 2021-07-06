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
        left = 2*i + 1
        right = left + 1

        while left < len(self.elements) - 1:
            higher = left if self.elements[left] > self.elements[right] else right

            if self.elements[higher] > self.elements[i]:
                temp = self.elements[i]
                self.elements[i] = self.elements[higher]
                self.elements[higher] = temp
                i = higher
            else:
                break

            left = 2*i + 1
            right = left + 1

        return out

    def is_empty(self):
        """
        Returns true if heap is empty, falses otherwise.
        """
        return len(self.elements) == 0

    def __str__(self) -> str:
        return " ".join([str(r) for r in self.elements])
