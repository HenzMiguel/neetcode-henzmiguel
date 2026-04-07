# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def recurse(root, s, target):
            if not root:
                return False

            s += root.val
            if target == s and not root.left and not root.right:
                return True
            
            left = recurse(root.left, s, target)

            right = recurse(root.right, s, target)

            return left or right
    

        return recurse(root, 0, targetSum)