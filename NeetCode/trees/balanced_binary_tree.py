'''
Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftDepth = checkBalance(root.left)
            if leftDepth == -1:
                return -1
            
            rightDepth = checkBalance(root.right)
            if rightDepth == -1:
                return -1
            
            if abs(leftDepth - rightDepth) > 1:
                return -1
            
            return 1 + max(leftDepth, rightDepth)
        return checkBalance(root) != -1


# Helper function to build a tree for testing
def createTree(nodes):
    if not nodes:
        return None
    val = nodes.pop(0)
    if not val:
        return None
    root = TreeNode(val)
    root.left = createTree(nodes)
    root.right = createTree(nodes)
    return root

# Test cases
sol = Solution()

# Balanced tree
root1 = createTree([3, 9, None, None, 20, 15, None, None, 7])
print(sol.isBalanced(root1))  # True

# Unbalanced tree
root2 = createTree([1, 2, 3, 4, None, 5, None, 6])
print(sol.isBalanced(root2))  # False


# Single node tree
root3 = createTree([1])
print(sol.isBalanced(root3))  # True

# Empty tree
print(sol.isBalanced(None))  # True
