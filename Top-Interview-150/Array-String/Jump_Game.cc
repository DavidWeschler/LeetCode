/*
----------------------------
Leetcode: Top-Interview-150
Array / String
Jump Game

Time complexity: O(N)
Space complexity: O(1)
----------------------------

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise. 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goalPost = nums.size()-1;

        for (int i=goalPost-1; i >= 0; i--) {
            if (nums[i]+i >= goalPost) {
                goalPost = i;
            }
        }

        return goalPost == 0;
    }
};


int main() {
    vector<int> nums = {2,3,1,1,4};
    // vector<int> nums = {3,2,1,0,4};
    Solution solution;

    bool can = solution.canJump(nums);

    if (can) cout << "True";
    else cout << "False";

}