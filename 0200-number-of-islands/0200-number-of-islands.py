class Solution(object):
    def dfs(self, row, col, vis, grid):
        vis[row][col] = 1
        directions = [(-1,0), (0,1), (1,0),(0,-1)]
        for r,c in directions:
            nr = row+r
            nc = col+c

            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]!=1 and grid[nr][nc] == "1":
                self.dfs(nr, nc, vis, grid)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        vis = [[0]*n  for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, vis, grid)
        return count