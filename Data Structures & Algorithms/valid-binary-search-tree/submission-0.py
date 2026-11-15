# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isbst(self, root, l, r):
        if not root:
            return True
        if not (r >= root.val >= l):
            return False
        left = self.isbst(root.left, l, root.val-1)
        right = self.isbst(root.right, root.val+1, r)

        if left and right:
            return True
        return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isbst(root, -math.inf, math.inf)