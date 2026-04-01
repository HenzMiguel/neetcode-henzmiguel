# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)
        
        node = root
        while node != None:
            if node.val <= val:
                if node.right == None:
                    node.right = TreeNode(val=val)
                    break
                node = node.right
            else:
                if node.left == None:
                    node.left = TreeNode(val=val)
                    break
                node = node.left
        return root