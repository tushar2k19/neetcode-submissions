class Solution:
    def rec(self, n, nums, used, v, ans):
        if len(v) == n:
            ans.append(v[:])     # make a copy
            return
        
        for i in range(n):
            if not used[i]:
                used[i] = True
                v.append(nums[i])
                
                self.rec(n, nums, used, v, ans)
                
                v.pop()
                used[i] = False

    def permute(self, nums):
        n = len(nums)
        ans = []
        used = [False] * n
        v = []

        self.rec(n, nums, used, v, ans)
        return ans
