class Solution:
    def dfs(self, grid, vis,row, col, pr, pc):
        vis[row][col] = 1
        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        for r, c in directions:
            nr =  row+r
            nc = col + c
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[row][col] == grid[nr][nc]:
                if not vis[nr][nc] :
                    if self.dfs(grid, vis, nr, nc, row, col):
                        return True
                
                elif nr != pr or nc != pc:
                    return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j]:
                    if self.dfs(grid, vis, i, j, -1, -1):
                        return True
        return False