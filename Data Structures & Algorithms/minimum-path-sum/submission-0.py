import math
class Solution:
    def rec(self, i, j, n,m, grid):
        if i>=n or j>=m:
            return math.inf
        if i==n-1 and j == m-1:
            return grid[i][j]
        if self.dp[i][j]!=-1:
            return self.dp[i][j]

        r = self.rec(i+1, j, n, m, grid) 
        d = self.rec(i, j+1, n, m, grid)

        self.dp[i][j] = min(r, d) + grid[i][j]
        return self.dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m= len(grid[0])
        self.dp = [[-1 for x in range(m)] for y in range(n)]
        return self.rec(0,0, n,m, grid)
        