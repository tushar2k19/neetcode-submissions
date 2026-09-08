class Solution:
    def rec(self, i: int, nums: List[int], n:int) -> int:
        if i >= n:
            return 0
        if self.dp[i] is not -1:
            return self.dp[i]
    
        inc = self.rec(i+2, nums, n) + nums[i]
        exc = self.rec(i+1, nums, n)

        self.dp[i] = max(inc, exc)
        return self.dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        self.dp = [-1]*n

        ans1 =  self.rec(0, nums, n-1)
        self.dp = [-1]*n
        ans2 = self.rec(1,nums,n)
        return max(ans1,ans2)