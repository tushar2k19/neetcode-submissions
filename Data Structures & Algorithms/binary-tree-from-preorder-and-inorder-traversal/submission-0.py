# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, ps, pe, ins, ie, pre, ino, mp):  #pre_start, in_end, in_start
        if pe<ps or ie<ins:
            return None

        root = pre[ps]
        leng = mp[root]-ins

        left = self.rec(ps+1, ps + leng, ins, mp[root] - 1, pre, ino, mp)
        right = self.rec(ps+leng+1, pe, mp[root]+1, ie, pre, ino, mp)

        node = TreeNode(root, left, right)
        return node

    def buildTree(self, pre: list[int], ino: list[int]) -> TreeNode | None:
        mp= {}
        for i,x in enumerate(ino):
            mp[x] = i
        
        return self.rec(0, len(pre)-1, 0, len(ino)-1, pre, ino, mp)

        