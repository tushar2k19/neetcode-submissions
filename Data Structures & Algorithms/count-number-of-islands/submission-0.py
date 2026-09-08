class Solution:
    def dfs(self, i,j,n,m,grid):
        
        if (i<0 or j<0 or i==n or j==m or grid[i][j]=='0'):
            return
        if (i,j) in self.vis:
            return
        
        self.vis[(i,j)]=True

        options = [(-1,0), (1,0), (0,-1), (0,1)]
        for x in options:
            self.dfs(i+x[0], j+x[1], n,m, grid)
    def numIslands(self, grid: List[List[str]]) -> int:
        self.vis = defaultdict(bool)
        n, m = len(grid), len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if (i,j) not in self.vis and grid[i][j]=='1':
                    self.dfs(i,j,n,m,grid)
                    ans+=1
        return ans
        
