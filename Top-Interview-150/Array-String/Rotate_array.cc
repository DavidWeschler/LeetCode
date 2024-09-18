/*
----------------------------
Leetcode: Top-Interview-150
Array / String
Rotate Array

Time complexity: O(N)
Space complexity: O(N)
----------------------------

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> tempNums;
        for (int i=0; i<nums.size(); i++) {
            tempNums.push_back(nums[i]);
        }

        for (int counter = 0; counter < nums.size(); counter++) {
            nums[(k+counter)%nums.size()] = tempNums[counter];
        }
    }
};

int main() {
    std::vector<int> nums = {1,2,3,4,5,6,7, 8};
    // std::vector<int> nums = {-1,-100,3,99};
    Solution sulotion;

    sulotion.rotate(nums, 2);

    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }

    return 0;
}