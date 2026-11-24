class Solution:
    def dfs(self, i: int, j: int, hts: List[List[int]], vis: List[List[int]], n: int, m: int):
        if i<0 or j<0 or i>=n or j>=m:
            return 
        vis[i][j] = 1
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and hts[ni][nj] >= hts[i][j]:
                self.dfs(ni, nj, hts, vis, n, m)

    def pacificAtlantic(self, hts: List[List[int]]) -> List[List[int]]:
        n, m = len(hts), len(hts[0])
        vis = [[0] * m for _ in range(n)]
        vis2 = [[0] * m for _ in range(n)]

        for i in range(n):
            self.dfs(i, 0, hts, vis, n, m)
        for j in range(m):
            self.dfs(0, j, hts, vis, n, m)

        for i in range(n - 1, -1, -1):
            self.dfs(i, m - 1, hts, vis2, n, m)
        for j in range(m - 1, -1, -1):
            self.dfs(n - 1, j, hts, vis2, n, m)

        ans = []
        for i in range(n):
            for j in range(m):
                if vis[i][j] and vis2[i][j]:
                    ans.append([i, j])
        return ans