# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val:
            def recurse(node, subnode):
                if (not node and subnode) or (node and not subnode):
                    return False 
                elif not node and not subnode:
                    return True

                if node.val != subnode.val:
                    return False

                l = recurse(node.left, subnode.left)

                r = recurse(node.right, subnode.right)

                return l and r
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return recurse(root, subRoot) or l or r

        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r