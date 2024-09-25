'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"

Output: true

Example 2:
Input: s = "jar", t = "jam"

Output: false

Constraints:
s and t consist of lowercase English letters.

'''
# Time complexity: O(s+t)

# from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False
        
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        for l in s_hash.keys():
            if l not in t_hash.keys() or s_hash[l] != t_hash[l]:
            # if s_hash[l] != t_hash.get(l, 0):
                return False
        
        return True
    

    #Note: we can write the whole func in 1 line of code: return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))
