'''
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
[1, 2, 3, 4 ]
[10,11,12,13]
[14,20,30,40]

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
[1, 2, 4, 8 ]
[10,11,12,13]
[14,20,30,40]

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:      # empty matrix
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        if target > matrix[rows-1][cols-1]:   # if the target is larger than the biggest element
            return False

        # finding the row:
        l, r = 0, rows-1
        rowIndex = None
        while l <= r:
            middle = (l+r)//2
            if matrix[middle][cols-1] == target:
                return True
            elif matrix[middle][cols-1] > target:
                if middle == 0 or matrix[middle-1][cols-1] < target:
                    rowIndex = middle
                    break
                else:
                    r = middle - 1
            else:
                l = middle + 1
        
        return self.search(matrix[rowIndex], target) != -1


    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while True:
            # middle = (l + r) // 2
            middle = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
            if l > r:
                return -1


sol = Solution()

# 1. Target is present in the matrix (basic case)
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10) == True  # Target 10 is in the matrix

# 2. Target is present at the end of the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 40) == True  # Target 40 is the last element

# 3. Target is present at the beginning of the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 1) == True   # Target 1 is the first element

# 4. Target is in the middle of the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 12) == True  # Target 12 is in the middle

# 5. Target is not present in the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15) == False  # Target 15 is not present

# 6. Target is larger than the largest element in the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 50) == False  # Target 50 exceeds matrix max

# 7. Target is smaller than the smallest element in the matrix
assert sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 0) == False   # Target 0 is smaller than the min

# 8. Matrix with only one row and target is present
assert sol.searchMatrix([[1, 3, 5, 7, 9]], 5) == True  # Single row, target 5 is present

# 9. Matrix with only one row and target is absent
assert sol.searchMatrix([[1, 3, 5, 7, 9]], 8) == False  # Single row, target 8 is absent

# 10. Matrix with only one column and target is present
assert sol.searchMatrix([[1], [3], [5], [7], [9]], 7) == True  # Single column, target 7 is present

# 11. Matrix with only one column and target is absent
assert sol.searchMatrix([[1], [3], [5], [7], [9]], 6) == False  # Single column, target 6 is absent

# 12. Target is present in the middle of the matrix
assert sol.searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == True  # Target 5 is at the center

# 13. Empty matrix (edge case)
assert sol.searchMatrix([], 5) == False  # No elements in the matrix

print("All test cases passed!")
