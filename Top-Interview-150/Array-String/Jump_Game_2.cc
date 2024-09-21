/*
----------------------------
Leetcode: Top-Interview-150
Array / String
Jump Game 2

Time complexity: O(N)
Space complexity: O(1)
----------------------------
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int start = 0,
            end = 0,
            jumps = 0,
            far = 0;

        for (; far < nums.size()-1;) {
            far = 0;

            for (int i=start; i<=end; i++) {
                far = std::max(far, i+nums[i]);
            }

            start = end+1;
            end = far;
            jumps++;
        }
        return jumps;
    }
};

int main() {
    vector<int> nums = {2,7,1,1,4, 2, 1, 9, 4};
    Solution solution;
    cout << solution.jump(nums);
}