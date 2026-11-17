# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root, k):
        if not root or self.count>=k:
            return
        self.rec(root.left, k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
            return

        self.rec(root.right, k)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count  = 0
        self.ans = math.inf
        self.rec(root,k)
        return self.ans
          