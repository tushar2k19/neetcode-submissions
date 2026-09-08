class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n,m  = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
        time = 0
        while q:
            front = q.popleft()
            options = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            time = max(time, front[2])
            # print("-----------------")
            # print("for top =", front)
            for x in options:
                ni,nj = front[0] + x[0], front[1]+x[1]
                # print(ni,nj)
                if ni >=0 and ni<n and nj>=0 and nj<m and grid[ni][nj]==1:
                    # print("goes inside- ", ni,nj)
                    q.append((ni, nj, front[2]+1))
                    grid[ni][nj] = 2
            # print(q)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return time


            
        