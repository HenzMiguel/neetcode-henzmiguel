def recurse(node):
    if node is None:
        return [True, 0]

    left = recurse(node.left)
    right = recurse(node.right)

    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

    return [balanced, 1 + max(left[1], right[1])]

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return recurse(root)[0]