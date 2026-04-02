# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, val, sub):
    if node == None:
        return

    if node.val == val:
        sub.append(node)

    dfs(node.left, val, sub)
    dfs(node.right, val, sub)
    
    return

def IsSame(subgraph, graph, istrue):
    if (subgraph != None and graph == None) or (subgraph == None and graph != None):
        istrue[0] = False
        return
    
    if subgraph == None and graph == None:
        return
    
    if subgraph.val != graph.val:
        istrue[0] = False
        return

    IsSame(subgraph.left, graph.left, istrue)
    IsSame(subgraph.right, graph.right, istrue)

    return 

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        getSub = []
        dfs(root, subRoot.val, getSub)

        for candidate in getSub:
            res = [True]
            IsSame(subRoot, candidate, res)
            if res[0]:
                return True

        return False