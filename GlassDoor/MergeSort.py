'''
Given 1 to 1000 numbers in random order how do you sort it efficiently
Answer 2: merge sort - O(nlogn)
'''

def mergeSort(arr: list[int]):
    n = len(arr)
    if n <= 1:
        return
    
    left = arr[0 : n//2]
    right = arr[n//2 : ]
    mergeSort(left)
    mergeSort(right)

    # merge l and r
    arr.clear()
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1
    
    while l < len(left):
        arr.append(left[l])
        l+=1
    while r < len(right):
        arr.append(right[r])
        r+=1

if __name__ == "__main__":
    array = [4, 1, -9, 0]
    mergeSort(array)
    print(array)