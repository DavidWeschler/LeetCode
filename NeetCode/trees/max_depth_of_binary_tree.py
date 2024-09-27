'''
Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftMax = 1 + self.maxDepth(root.left)
        rightMax = 1 + self.maxDepth(root.right)

        return max(leftMax, rightMax)  

def buildTree(values, index=0) -> Optional[TreeNode]:
    """Build a tree from a list of values in level order."""
    if index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = buildTree(values, 2 * index + 1)
    root.right = buildTree(values, 2 * index + 2)
    return root

# Test case:
if __name__ == '__main__':
    sol = Solution()
    root = buildTree([3, 9, 20, None, None, 15, 7])
    print("Maximum depth of the tree:", sol.maxDepth(root))  # Expected output: 3
