# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(node, l):
    if node is None:
        return None

    recurse(node.left, l)
    l.append(node.val)
    recurse(node.right, l)

    return l

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        recurse(root, res) 

        return res