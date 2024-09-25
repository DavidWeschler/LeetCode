'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''

from typing import List 

#Time complexity: O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]

#Time complexity: O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, num in enumerate(nums):
            complete = target - num
            if complete in hashmap:
                return [hashmap[complete], index]
            hashmap[num] = index

    
sol = Solution()
sol2 = Solution2()
# print(sol.twoSum([3,4,5,6], 7))
# print(sol.twoSum([4,5,6], 10))
# print(sol.twoSum([5,5], 10))
# print(sol2.twoSum([4, 5, 6], 10))
print(sol2.twoSum([3, 4, 5, 6], 7))