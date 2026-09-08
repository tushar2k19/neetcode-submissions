class Solution:

    def rec(self, n:int, dp: List[int])-> int:
        if n ==1 or n==0:
            dp[n] = 1
            return dp[n]

        if dp[n]!=-1:
            return dp[n]
        
        dp[n] = self.rec(n-1, dp) + self.rec(n-2,dp)

        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)

        return self.rec(n,dp)
        
        