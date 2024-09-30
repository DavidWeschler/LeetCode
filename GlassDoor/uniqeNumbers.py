'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

from typing import List

# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return True
        arr.sort()
        occur = {}
        curr = 0
        currNum = arr[0]
        for i in range(len(arr)):
            if arr[i] != currNum:
                if curr in occur:
                    return False
                else:
                    occur[curr] = currNum
                    curr = 0
                    currNum = arr[i]
            curr += 1
        return not curr in occur

# class Solution2:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))
    print(sol.uniqueOccurrences([1,2]))
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))