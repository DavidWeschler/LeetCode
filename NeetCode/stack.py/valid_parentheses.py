'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false

Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000

'''


class Solution:
    def isValid(self, s: str) -> bool:
        circel, square, curly = 0, 0, 0
        stack = []
        for char in s:
            if char == '(':
                circel += 1
                stack.append(')')
            elif char == '[':
                square += 1
                stack.append(']')
            elif char == '{':
                curly += 1
                stack.append('}')
            elif stack == [] or char != stack[-1]:
                return False
            elif char == stack[-1]:
                stack.pop()
            
        return stack == []
    

# websites solution
class Solution2:    
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

# Creating an instance of the Solution class
sol = Solution()

# 1. Basic Valid Parentheses (Single Type)
assert sol.isValid("[]") == True  # Basic valid case with square brackets
assert sol.isValid("()") == True  # Valid case with round brackets
assert sol.isValid("{}") == True  # Valid case with curly brackets

# 2. Multiple Mixed Valid Parentheses
assert sol.isValid("([{}])") == True  # Mixed types, valid nested case
assert sol.isValid("{[()]}") == True  # Another valid nested case
assert sol.isValid("{{[]}}") == True  # Nested valid case with curly and square brackets

# 3. Invalid Parentheses
assert sol.isValid("[(])") == False  # Incorrect order, should return False
assert sol.isValid("[[") == False    # Missing closing brackets
assert sol.isValid("{{]") == False   # Mismatched brackets

# 4. Empty String
assert sol.isValid("") == True  # An empty string is considered valid

# 5. Only Closing Brackets
assert sol.isValid("}}]") == False  # Only closing brackets without matching opening

# 6. Only Opening Brackets
assert sol.isValid("{{[[") == False  # Only opening brackets without closing

# 7. Complex Valid Case
assert sol.isValid("{[()]({[]})}") == True  # Complex case with nested and sequential valid brackets

# 8. Complex Invalid Case
assert sol.isValid("{[()]}{[)]") == False  # Invalid case, the last pair of brackets is mismatched

# 9. Mismatched Brackets
assert sol.isValid("[{]}") == False  # Incorrect closing order

# 10. Invalid but Correct Number of Brackets
assert sol.isValid("([)]") == False  # The number of brackets matches, but the order is incorrect

print("All test cases passed!")
