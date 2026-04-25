class Solution(object):
    def dfs(self, vis, grid, sr, sc):
        count = 1
        vis[sr][sc] = 1
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        for r,c in directions:
            nr = sr+r
            nc = sc + c
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and not vis[nr][nc] and grid[nr][nc]==1:
                count += self.dfs(vis,grid, nr, nc)
        return count
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vis = [[0]*len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1) and not vis[i][j] and grid[i][j]==1:
                    self.dfs(vis, grid, i, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j] and grid[i][j] == 1:
                    ans += self.dfs(vis, grid, i, j)
                    
        return ans
        