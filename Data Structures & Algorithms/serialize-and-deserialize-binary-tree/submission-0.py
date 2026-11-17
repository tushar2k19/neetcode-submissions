# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def rec1(self, root):
        if not root:
            return "N"
        s1 = self.rec1(root.left)
        s2 = self.rec1(root.right)
        
        s = str(root.val) + "," + s1 + "," + s2 

        return s

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        s = self.rec1(root)
        print(s)
        return s
        

    def deserialize(self, s: str) -> Optional[TreeNode]:
        arr = s.split(",")
        arr = [int(x) if x!='N' else x for x in arr]
        self.i = 0
        def rec2(arr):
            val = arr[self.i]
            self.i+=1
            if val == 'N':
                return None
            left = rec2(arr)
            right = rec2(arr)
            
            node = TreeNode(val, left, right)
            
            return node

        ans = rec2(arr)
        return ans
