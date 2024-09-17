/*
----------------------------
Leetcode: Top-Interview-150
Array / String
Majority Element

Time complexity: O(nlogn)
Space complexity: O(nlogn)
----------------------------
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

*/

#include <iostream>
#include <vector>
#include <algorithm> // for std::sort

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int amount = 1;
        for (int i=1; i<nums.size(); i++) {
            amount++;
            if (nums[i] != nums[i-1]) {
                amount = 1;
            } else if (amount > nums.size()/2) {
                return nums[i];
            }
        }
        return nums[0];
    }
};

int main() {
    std::vector<int> nums = {1,1,2,1,2,2,2,4,2,2};
    Solution sulotion;

    int k = sulotion.majorityElement(nums);

    cout << k << endl;
    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }

    return 0;
}