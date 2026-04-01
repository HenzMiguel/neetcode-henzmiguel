# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, s):
    if node == None:
        return s

    left = dfs(node.left, s + 1)

    right = dfs(node.right, s + 1)

    return max(left, right, s)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return dfs(root, 0)