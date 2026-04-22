class Solution:
    fresh = 0
    def bfs(self, queue, grid):
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        sr,sc = queue.pop(0)
        print(grid[sr][sc])
        for r,c in directions:
            nr = sr+r
            nc = sc+c
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                grid[nr][nc] = 2
                self.fresh -= 1
                queue.append(tuple([nr, nc]))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    isRottFound = True
                    queue.append(tuple([i, j]))
                if grid[i][j] == 1:
                    self.fresh += 1
        time = 0
        while len(queue)>0 and self.fresh > 0:
            for _ in range(len(queue)):
                self.bfs(queue, grid)
            time += 1
        return time if self.fresh==0 else -1
            
        