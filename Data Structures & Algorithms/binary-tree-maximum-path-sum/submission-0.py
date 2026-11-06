# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        ls = self.rec(root.left)
        rs = self.rec(root.right)
        self.ans = max(self.ans, max(0,ls)+max(0,rs) + root.val)

        return root.val + max(0,max(ls,rs))  #dont consider the negative childs

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = -math.inf
        self.rec(root)
        return self.ans
        

        