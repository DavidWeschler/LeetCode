'''
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Given the root of a binary tree root, return the diameter of the tree.

Example 1:
Input: root = [1,null,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:
Input: root = [1,2,3]
Output: 2

Constraints:
1 <= number of nodes in the tree <= 100
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftMax = maxDepth(root.left)
            rightMax = maxDepth(root.right)
            
            self.diameter = max(self.diameter, leftMax + rightMax)
            
            return 1 + max(leftMax, rightMax) 
        
        maxDepth(root)
        return self.diameter

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

    # Example 1: [1, 2, 3, 4, 5]
    root = buildTree([1, 2, 3, 4, 5])
    print(sol.diameterOfBinaryTree(root))  # Expected output: 3
    
    # Example 2: [1, 2, None, 3, None, 4, None, 5]
    root = buildTree([1, 2, None, 3, None, 4, None, 5])
    print(sol.diameterOfBinaryTree(root))  # Expected output: 4
    
    # Example 3: [1]
    root = buildTree([1])
    print(sol.diameterOfBinaryTree(root))  # Expected output: 0
