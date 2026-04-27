class Solution:
    def dfs(self, vis, grid,directions, row, col):
        if row==len(grid)-1 and col==len(grid[0])-1:
            return True
        vis[row][col] = 1
        for dx, dy in directions[grid[row][col]]:
            nr = row+dx
            nc = col+dy
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and not vis[nr][nc]:
                if (-dx, -dy) in directions[grid[nr][nc]]:
                    if self.dfs(vis, grid, directions, nr, nc):
                        return True
        return False
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)], #left to right
            2:[(-1,0), (1,0)], #up to down
            3: [(0, -1), (1,0)], #left to down
            4: [(0,1), (1,0)], #right to down
            5: [(0, -1), (-1, 0)], #left to up
            6:[(0, 1),(-1, 0)], #right to up

        }

        vis = [[0]*len(grid[0]) for i in range(len(grid))]
        return self.dfs(vis, grid, directions, 0, 0)
