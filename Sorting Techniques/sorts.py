"""
Code for various sorting algos.
"""

import unittest
class Node:
    """
    Object Node
    ...
    Attributes:
    ----------
    data (int) : data for the node
    next (Node) : Points to the next node

    Methods:
    -------
    get_data(): returns data of the node
    """
    def __init__(self, data):
        """
        Constructor function
        parameters:
        data (int) : data for the node.
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Getter function for self.data
        """
        return self.data
def bubble_sort(arr):
    """
    Bubble Sort:
    Time Complexity : O(n^2)
    Stable
    Adaptive
    """
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1

        if flag == 0:
            break

    return arr

def selection_sort(arr):
    """
    Selection Sort:
    Time Complexity : O(n^2)
    Not Stable
    Not Adaptive
    """
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    
    return arr

def insertion_sort(arr):
    """
    Insertion Sort:
    Time Complexity : O(n^2)
    Stable
    Adaptive
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = current

    return arr

def quick_partition(arr, start, end):
    """
    Method for creating partitioning arrays for quick sort.
    """
    pivot = arr[start]
    pivot_index = start

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        
        while pivot < arr[end]:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end

def quick_sort(arr, start, end):
    """
    Insertion Sort:
    Time Complexity : O(n^2)
    Not Stable
    Adaptive
    """
    if start < end:
        p = quick_partition(arr, start, end)

        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)
    return arr

def merge(arr, start, mid, end):
    """
    Method for merging 2 arrays.
    """
    i, j, k = 0, 0, start

    # Temporary lists for left and right partitions.
    L = [arr[r] for r in range(start, mid+1)]
    R = [arr[r] for r in range(mid+1, end+1)]

    # Loop for sorting elements in the [start, end] range,
    # By choosing smaller elements among two partitions.
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Adding rest of the elements of each partition.
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_two(arr1, arr2):
    """
    Method for merging 2 arrays.
    """
    i = j = 0
    arr3 = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

def merge_sort(arr, start, end):
    """
    Merge Sort:
    Time Complexity : O(n log(n))
    Stable
    Adaptive
    """
    if start < end:
        mid = (start+end) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)

        merge(arr, start, mid, end)

    return arr
        
def radix_sort(arr):
    """
    Count Sort:
    Time Complexity : O(dn)
    Stable
    Adaptive
    """
    RADIX = 10
    divisor = 1
    biggest = max(arr)

    while divisor < biggest:
        arr2 = [None for r in range(10)]

        for r in arr:
            temp = int((r / divisor) % RADIX)
            if arr2[temp] == None:
                arr2[temp] = Node(r)
            else:
                current = arr2[temp]
                while current.next:
                    current = current.next
                current.next = Node(r)

        k = 0
        for r in arr2:
            current = r
            while current:
                arr[k] = r.data
                k += 1
                current = current.next

        divisor *= RADIX
    return arr

def shell_sort(arr):
    """
    Count Sort:
    Time Complexity : O(n^2)
    Stable
    Adaptive
    """
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap
        
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1
        
        while i - gap > -1:
            if arr[i] < arr[i - gap]:
                arr[i], arr[i - gap] = arr[i - gap], arr[i]
            
            i -= 1
        
        gap //= 2
    
    return arr


def count_sort(arr):
    """
    Count Sort:
    Time Complexity : O(n)
    Stable
    Adaptive
    """
    biggest = max(arr)
    arr2 = [0 for r in range(biggest)]

    for r in arr:
        arr2[r-1] += 1

    k = 0
    for r in range(len(arr2)):
        for i in range(arr2[r]):
            arr[k] = r + 1
            k += 1

    return arr

def bit_bucket_sort(arr):
    """
    Count Sort:
    Time Complexity : O(n^2)
    Stable
    Adaptive
    """
    biggest = max(arr)
    arr2 = [None for r in range(biggest)]

    for r in arr:
        if arr2[r-1] == None:
            arr2[r-1] = Node(r)
        else:
            current = arr2[r-1]
            while current.next:
                current = current.next
            current.next = Node(r)
    
    k = 0
    for r in arr2:
        current = r
        while current:
            arr[k] = r.data
            k += 1
            current = current.next

    return arr


class TestSortAlgos(unittest.TestCase):
    def test_bubble(self):
        arr = [r for r in range(5, 0, -1)]
        self.assertEqual(sorted(arr), bubble_sort(arr))

    def test_insertion(self):
        arr = [r for r in range(5, 0, -1)]
        self.assertEqual(sorted(arr), insertion_sort(arr))
    
    def test_selection(self):
        arr = [r for r in range(5, 0, -1)]
        self.assertEqual(sorted(arr), selection_sort(arr))

    def test_quick(self):
        arr = [5,1,2,3,9,3,1,4]
        self.assertEqual(sorted(arr), quick_sort(arr, 0, len(arr)-1))
        
    def test_merge(self):
        arr = [5,1,2,3,2,8,6,4]
        self.assertEqual(sorted(arr), merge_sort(arr, 0, len(arr) - 1))
        
    def test_radix(self):
        arr = [5,2,9,2,3,4]
        self.assertEqual(sorted(arr), radix_sort(arr))
        
    def test_shell(self):
        arr = [5,2,2,4,9,4]
        self.assertEqual(sorted(arr), shell_sort(arr))
        
    def test_count(self):
        arr = [5,1,2,2,4,9,2,2,4]
        self.assertEqual(sorted(arr), count_sort(arr))
        
    def test_bit_bucket(self):
        arr = [5,1,2,2,4,9,5,6,6]
        self.assertEqual(sorted(arr), bit_bucket_sort(arr))
        
    
if __name__ == "__main__":
    unittest.main()