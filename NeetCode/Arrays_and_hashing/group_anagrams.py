'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(str: str, word: str) -> bool:
            if (len(str) != len(word)):
                return False
            str = sorted(str)
            word = sorted(word)

            for i in range(len(str)):
                if str[i] != word[i]:
                    return False
            
            return True
        
        seen = {}
        result = []
        for i in range(len(strs)):
            temp = []
            for s in strs:
                if not s in seen and isAnagram(s, strs[i]):
                    temp.append(s)
                    seen[s] = True
            if temp:
                result.append(temp)
        
        return result

if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))