from collections import deque
class Solution:
    def bfs(self, grid, queue):
        count = 0
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        sr,sc = queue.popleft()
        for cr, cc in directions:
            nr=cr+sr
            nc = cc+sc
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                grid[nr][nc] = 2
                count+=1
                queue.append((nr, nc))
        return count
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    freshCount += 1
        timeTaken = 0
        rottedMango = 0
        while queue and rottedMango<  freshCount:
            rottedMangoPerMinute = len(queue)
            for i in range(rottedMangoPerMinute):
                rottedMango += self.bfs(grid, queue)
            timeTaken+=1
        
        return timeTaken if rottedMango==freshCount else -1