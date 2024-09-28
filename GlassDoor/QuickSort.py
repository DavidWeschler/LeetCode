'''
Given 1 to 1000 numbers in random order how do you sort it efficiently
Answer 3: quick sort - O(nlogn) on average, wors case O(n^2)
'''

def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo+1
    j = hi

    while True:
        while i <= hi and arr[i] <= pivot:
            i += 1
        while j >= lo and arr[j] > pivot:
            j -= 1
        
        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
    
    arr[lo], arr[j] = arr[j], arr[lo]

    return j


def quickSort(arr, lo, hi):
    if hi <= lo:
        return

    pivotIndex = partition(arr, lo, hi)

    quickSort(arr, lo, pivotIndex-1)
    quickSort(arr, pivotIndex+1, hi)


def myQuickSort(arr):
    quickSort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    array = [4, 1, -9, 0]
    myQuickSort(array)
    print(array)