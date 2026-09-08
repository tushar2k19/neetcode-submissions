class Solution:
    def rec(self, cost: List[int], n: int) -> int:
        if n == 0 or n==1:
            return 0
        if self.dp[n] is not -1:
            return self.dp[n]
        self.dp[n] = min(self.rec(cost, n-1) + cost[n-1], self.rec(cost, n-2) + cost[n-2])
        return self.dp[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        self.dp = [-1]*(n+1)

        return self.rec(cost, n)
        