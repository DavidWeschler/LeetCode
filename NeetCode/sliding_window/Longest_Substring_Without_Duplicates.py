'''
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.
'''

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        chars = {}

        for right in range(len(s)):
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            
            chars[s[right]] = right
            maxLen = max(maxLen, right-left+1)

        return maxLen

sol = Solution()

# 0. test
assert sol.lengthOfLongestSubstring("abba") == 2

# 1. Basic test case with unique substring
assert sol.lengthOfLongestSubstring("zxyzxyz") == 3  # "xyz" is the longest substring without repeating characters


# 2. All characters are the same
assert sol.lengthOfLongestSubstring("xxxxx") == 1  # Only one unique character, so the longest substring is of length 1

# 3. No repeating characters
assert sol.lengthOfLongestSubstring("abcdefg") == 7  # Entire string is unique

# 4. A string with all repeated characters except one
assert sol.lengthOfLongestSubstring("bbbbb") == 1  # Only one unique character

# 5. Alternating characters
assert sol.lengthOfLongestSubstring("ababab") == 2  # "ab" is the longest unique substring

# 6. Single character
assert sol.lengthOfLongestSubstring("a") == 1  # Only one character

# 7. Empty string
assert sol.lengthOfLongestSubstring("") == 0  # No characters in the string, so length is 0

# 8. String with spaces
assert sol.lengthOfLongestSubstring("abc abc") == 4  # "abc " is the longest substring without repeating characters

# 9. Substring appears at the end
assert sol.lengthOfLongestSubstring("pwwkew") == 3  # "wke" is the longest substring without repeating characters

# 10. Longest substring in the middle
assert sol.lengthOfLongestSubstring("dvdf") == 3  # "vdf" is the longest unique substring

# 11. Case sensitivity test
assert sol.lengthOfLongestSubstring("AaBbCcDdEe") == 10  # All characters are unique, case sensitive

# 12. Numbers and letters
assert sol.lengthOfLongestSubstring("abc123abc123") == 6  # "abc123" is the longest unique substring

print("All test cases passed!")


      