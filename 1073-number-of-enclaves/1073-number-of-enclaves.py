class Solution(object):
    def outsideMarkingDfs(self, vis, grid, sr, sc ):
        vis[sr][sc] = 1
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        for r,c in directions:
            nr = sr+r
            nc = sc + c
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and not vis[nr][nc] and grid[nr][nc]==1:
                self.outsideMarkingDfs(vis,grid, nr, nc)

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
        #top
        for i in range(len(grid[0])):
            if not vis[0][i] and grid[0][i]==1:
                self.outsideMarkingDfs(vis, grid, 0, i)
        #right
        for i in range(len(grid)):
            if not vis[i][len(grid[0])-1] and grid[i][len(grid[0])-1]==1:
                self.outsideMarkingDfs(vis, grid, i, len(grid[0])-1)
        #down
        for i in range(len(grid[0])):
            if not vis[len(grid)-1][i] and grid[len(grid)-1][i]==1:
                self.outsideMarkingDfs(vis, grid, len(grid)-1, i)
        #left
        for i in range(len(grid)):
            if not vis[i][0] and grid[i][0]==1:
                self.outsideMarkingDfs(vis, grid, i, 0)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j] and grid[i][j] == 1:
                    ans += self.dfs(vis, grid, i, j)
        return ans
        