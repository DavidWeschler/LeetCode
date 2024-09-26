'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro, buyPrice = 0, prices[0]

        for i in range(1, len(prices)):
            if prices[i] - buyPrice > maxPro:
                maxPro = prices[i] - buyPrice
            if prices[i] < buyPrice:
                buyPrice = prices[i]
        return maxPro

sol = Solution()

# 1. Basic case with a profit
assert sol.maxProfit([10, 1, 5, 6, 7, 1]) == 6  # Buy at 1, sell at 7

# 2. No profit possible (prices always decrease)
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0  # No opportunity to make a profit

# 3. Maximum profit is at the end of the array
assert sol.maxProfit([1, 2, 3, 4, 5, 6]) == 5  # Buy at 1, sell at 6

# 4. Prices remain the same (no profit)
assert sol.maxProfit([5, 5, 5, 5, 5]) == 0  # No opportunity to make a profit

# 5. Only one day (no transactions possible)
assert sol.maxProfit([10]) == 0  # No opportunity to make a profit

# 6. Minimum at the beginning and maximum at the end
assert sol.maxProfit([1, 100]) == 99  # Buy at 1, sell at 100

# 7. Maximum profit occurs in the middle
assert sol.maxProfit([1, 3, 2, 5, 4, 8, 6]) == 7  # Buy at 1, sell at 8

# 8. Large range with alternating peaks and valleys
assert sol.maxProfit([9, 2, 11, 1, 7, 5, 10]) == 9  # Buy at 1, sell at 10

# 9. Prices increase, then drop, and then increase again
assert sol.maxProfit([3, 6, 1, 9, 4, 12]) == 11  # Buy at 1, sell at 12

# 10. Random price fluctuations
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5  # Buy at 1, sell at 6

# 11. A single low price followed by a big spike
assert sol.maxProfit([1, 10]) == 9  # Buy at 1, sell at 10

# 12. No price movement
assert sol.maxProfit([5]) == 0  # No transactions possible

print("All test cases passed!")


'''
maxPro = 4
buyPrice = 1
'''