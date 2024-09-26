'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
'''

from typing import List

class Solution:
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

assert sol.search([-1,0,2,4,6,8], 4) == 3
assert sol.search([-1,0,2,4,6,8], 3) == -1

print("All test cases passed!")