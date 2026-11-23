class Solution:
    def rec(self, grid, i,j, n,m, vis):
        if i < 0 or j<0 or i>=n or j>=m or grid[i][j] =='0' or  vis[i][j]:
            return
        
        vis[i][j] = 1
        
        options = [(0,1), (1,0), (0,-1), (-1,0)]
        
        
        for x,y in options:
            self.rec(grid, i+x, j+y, n,m, vis)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        count = 0
        vis = [[0 for x in range(m)] for x in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]!='0' and not vis[i][j]:
                    self.rec(grid, i, j, n,m, vis)  
                    count+=1
        return count
        
            