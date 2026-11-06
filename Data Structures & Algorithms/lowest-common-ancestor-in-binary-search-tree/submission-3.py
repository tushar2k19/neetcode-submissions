# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.LCA = None
        return self.rec(root, p,q)

    def rec(self, root, p,q):
        if not root:
            return None
        if self.LCA:
            return self.LCA

        if root.val == p.val or root.val == q.val:
            return root 

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            self.LCA = root
            return root
        elif left:
            return left
        else:
            return right

