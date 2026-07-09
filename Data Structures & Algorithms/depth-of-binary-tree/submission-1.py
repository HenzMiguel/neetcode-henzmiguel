# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def recurse(node):
            if not node:
                return 1
            
            left = recurse(node.left)
            right = recurse(node.right)

            return max(left, right) + 1
        return recurse(root) - 1