class Solution:
    def dfs(self, vis, grid,directions, i, j):
        if i == len(grid)-1 and j == len(grid[0])-1:
            return True
        vis[i][j] = 1
        for dx, dy in directions[grid[i][j]]:
            nr = i + dx
            nc = j + dy
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not vis[nr][nc]:
                #checking the reverse direction
                if (-1*dx, -1*dy) in directions[grid[nr][nc]]:
                    if self.dfs(vis, grid, directions, nr, nc):
                        return True
        return False
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(1, 0), (0, 1)],    # down, right
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(-1, 0), (0, 1)]    # up, right
        }

        vis = [[0]*len(grid[0]) for i in range(len(grid))]
        return self.dfs(vis, grid,directions, 0,0)
