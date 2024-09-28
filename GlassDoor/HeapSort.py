'''
Given 1 to 1000 numbers in random order how do you sort it efficiently
Answer 1: heap sort - O(nlogn)
'''

# heap sort:

def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(array: list[int]):
    n = len(array)

    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.
    for i in range(n//2-1, -1, -1):
        heapify(array, n, i)

    # extracting the elements one by one and
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


array = [5, 1, 7, 5, 0]
heapSort(array)
print(array)