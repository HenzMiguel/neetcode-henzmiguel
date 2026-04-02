# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def IsSame(p, q, check):

    if (p != None and q == None) or (p == None and q != None):
        check[0] = False
        return
    
    if p == None and q == None:
        return
    
    if p.val != q.val:
        check[0] = False
        return

    IsSame(p.left,q.left,check)
    IsSame(p.right,q.right,check)


    return
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check = [True]

        IsSame(p,q,check)
        return check.pop()