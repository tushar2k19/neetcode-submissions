class Solution:
    def rec(self, i, j, n,m):
        if i>=n or j>=m:
            return 0
        if i==n-1 and j == m-1:
            return 1
        if self.dp[i][j]!=-1:
            return self.dp[i][j]

        r = self.rec(i+1, j, n, m)
        d = self.rec(i, j+1, n, m)

        self.dp[i][j] = r + d
        return r+d
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[-1 for x in range(n)] for y in range(m)]
        return self.rec(0,0, m,n)
        