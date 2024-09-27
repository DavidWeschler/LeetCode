'''
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# helper functions:
def buildTree(values, index=0) -> Optional[TreeNode]:
    """Build a tree from a list of values in level order."""
    if index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = buildTree(values, 2 * index + 1)
    root.right = buildTree(values, 2 * index + 2)
    return root

def printTree(root: Optional[TreeNode]):
    """Print the tree in level order."""
    if not root:
        print("Empty tree")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
    print(' '.join(result))

# Test case:
if __name__ == '__main__':
    sol = Solution()

    # Example 1: Tree [4, 2, 7, 1, 3, 6, 9]
    # Inverted Tree: [4, 7, 2, 9, 6, 3, 1]
    root = buildTree([4, 2, 7, 1, 3, 6, 9])
    print("Original tree:")
    printTree(root)

    inverted = sol.invertTree(root)
    print("Inverted tree:")
    printTree(inverted)
