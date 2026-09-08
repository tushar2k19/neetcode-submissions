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
        self.dp = [-1]*n

        return self.rec(0, nums, n)