def bubble_sort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1

        if flag == 0:
            break

    return arr

def insertion_sort(arr):
    pass

def selection_sort(arr):
    pass

def quick_sort(arr):
    pass

def merge_sort(arr):
    pass

def radix_sort(arr):
    pass

def shell_sort(arr):
    pass

def cout_sort(arr):
    pass

if __name__ == "__main__":
    # arr = [int(input()) for r in range(int(input("Enter the number of elements: ")))]
    arr = [r for r in range(5, 0, -1)]
    arr = bubble_sort(arr)
    print(arr)
    pass