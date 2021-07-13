"""
Code for various sorting algos.
"""

import unittest
import math

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
    i, j = start, mid + 1
    arr2 = []

    while i <= mid and j < end:
        if arr[i] < arr[j]:
            arr2.append(arr[i])
            i += 1
        else:
            arr2.append(arr[j])
            j += 1
    
    while i <= mid:
        arr2.append(arr[i])
        i += 1

    while j < len(arr):
        arr2.append(arr[j])
        j += 1
    
    return arr2

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

    return arr3

def merge_sort(arr, start, end):
    pass
        
def radix_sort(arr):
    pass

def shell_sort(arr):
    pass

def count_sort(arr):
    pass

def bit_bucket_sort(arr):
    pass


# arr = [int(input("Enter number of elements: ")) for r in range(int(input()))]

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
        arr = [5,1,2,3,4]
        self.assertEqual(sorted(arr), quick_sort(arr, 0, len(arr)-1))
        
    # def test_merge(self):
    #     self.assertEqual(sorted(arr), merge_sort(arr))
        
    # def test_radix(self):
    #     self.assertEqual(sorted(arr), radix_sort(arr))
        
    # def test_shell(self):
    #     self.assertEqual(sorted(arr), shell_sort(arr))
        
    # def test_count(self):
    #     self.assertEqual(sorted(arr), count_sort(arr))
        
    # def test_bit_bucket(self):
    #     self.assertEqual(sorted(arr), bit_bucket_sort(arr))
        
    
if __name__ == "__main__":
    print(merge_sort([5,1,9,3,2,8,4,10,7,6], 0, 9))
    unittest.main()