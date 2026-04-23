from collections import deque
class Solution:
    # def bfs(self, que, vis, grid):
    #     sr,sc = que.pop(0)
    #     vis[sr][sc] = 1
    #     directions = [(-1, 0), (0,1), (1,0),(0,-1)]
    #     for r,c in directions:
    #         nr = sr+r
    #         nc = sc+c
    #         if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and not vis[nr][nc] :
    #             que.append(tuple([nr, nc]))
        
    # def findNearestZero(self, grid, sr, sc):
    #     que = []
    #     vis = [[0]*len(grid[0]) for i in range(len(grid))]
    #     que.append(tuple([sr,sc]))
    #     ans = 0
    #     isZeroFound = False
    #     while len(que)>0:
    #         for _ in range(len(que)):
    #             self.bfs(que, vis, grid)
    #         ans += 1
    #         for r,c in que:
    #             if grid[r][c] == 0:
    #                 isZeroFound = True
    #                 break
    #         if isZeroFound:
    #             break
    #     return ans
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 1:
        #             mat[i][j] = self.findNearestZero(mat, i, j)
        # return mat

        rcount, ccount = len(mat), len(mat[0])
        queue = deque()

        for i in range(rcount):
            for j in range(ccount):
                if mat[i][j] == 0:
                    queue.append(tuple([i,j]))
                else:
                    mat[i][j] = -1
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        while queue:
            cr, cc = queue.popleft()
            
            for r, c in directions:
                nr , nc = cr+r, cc + c
                if 0<=nr<rcount and 0<=nc<ccount and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[cr][cc] + 1
                    queue.append(tuple([nr, nc]))
        return mat
