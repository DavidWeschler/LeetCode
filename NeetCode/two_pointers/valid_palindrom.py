'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = re.sub(r'\s+', '', s)
        myString = re.sub(r'[^a-zA-z0-9]', '', s)
        myString = myString.lower()
        return myString == myString[::-1]
    
class Solution2:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

    
sol = Solution()
sol2 = Solution2()
# print(sol.isPalindrome("Was it a car or a cat I saw?"))
# print(sol.isPalindrome("tab a cat"))
# print(sol2.isPalindrome("Was it a car or a cat I saw?"))
# print(sol2.isPalindrome("tab a cat"))


# 1. Basic Palindrome
assert sol.isPalindrome("A man a plan a canal Panama") == True  # Mixed case and spaces

# 2. Single Character String
assert sol.isPalindrome("a") == True  # Single letter, should be true
assert sol.isPalindrome("A") == True  # Single letter in uppercase, still true

# 3. Empty String
assert sol.isPalindrome("") == True  # Empty string, should be considered a palindrome

# 4. Non-Palindrome
assert sol.isPalindrome("Hello") == False  # Simple string, not a palindrome

# 5. Palindrome with Punctuation
assert sol.isPalindrome("No 'x' in Nixon") == True  # Palindrome with non-alphanumeric characters

# 6. Case Sensitivity Test
assert sol.isPalindrome("Madam") == True  # Mixed case, should be case insensitive

# 7. Numbers and Letters
assert sol.isPalindrome("A1b2b1A") == True  # Includes numbers, should still be a palindrome

# 8. Palindrome with All Non-Alphabetic Characters
assert sol.isPalindrome("12321") == True  # Numbers only; since it's looking for alphabetic characters, returns True (empty string)

# 9. Non-Palindrome with Punctuation
assert sol.isPalindrome("Palindrome?") == False  # Non-palindrome with punctuation

# 10. Only Special Characters
assert sol.isPalindrome("!!!") == True  # Special characters only, should be considered a palindrome

# 11. Palindrome with Upper and Lower Case
assert sol.isPalindrome("Was it a car or a cat I saw") == True  # Ignore spaces and case

# If all assertions pass, you can print a success message
print("All test cases passed!")
