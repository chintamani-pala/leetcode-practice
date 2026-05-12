# import math
# class Solution:
#     def rotateOneTime(self, grid, irow, icol, jrow, jcol, krow,kcol, lrow, lcol):
#         if irow < len(grid) and icol < len(grid[0]):
#             prev = grid[irow][icol]

#         for i in range(irow+1, jrow+1):
#             grid[i][icol], prev = prev, grid[i][icol]
        
#         for i in range(jcol+1, kcol+1):
#             grid[jrow][i] , prev = prev, grid[jrow][i]

#         for i in range(krow-1, lrow-1, -1):
#             grid[i][kcol] , prev = prev, grid[i][kcol]
        
#         for i in range(lcol-1, icol-1, -1):
#             grid[irow][i], prev = prev, grid[irow][i]
        


#     def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         rowLen = len(grid)
#         colLen = len(grid[0])
#         # def rotateOneTIme(grid, irow, icol, jrow, jcol, krow,kcol, lrow, lcol):
#         irow, icol, jrow, jcol, krow,kcol, lrow, lcol = 0, 0, rowLen-1, 0, rowLen-1, colLen-1, 0, colLen-1
#         maxIter = math.ceil(min(colLen, rowLen)/2)
#         while maxIter > 0:
#             for i in range(k):
#                 self.rotateOneTime(grid, irow, icol, jrow, jcol, krow,kcol, lrow, lcol)
            
#             irow, icol, jrow, jcol, krow,kcol, lrow, lcol = irow+1, icol+1, jrow-1, jcol+1, krow-1, kcol-1, lrow+1, lcol-1
#             maxIter -= 1
#         return grid

class Solution:
    def rotateEachLevelKtimes(self, grid, top, bottom, left, right, k):
        elements = []

        # top -> bottom
        for i in range(top, bottom + 1):
            elements.append(grid[i][left])

        # left -> right
        for j in range(left + 1, right + 1):
            elements.append(grid[bottom][j])

        # bottom -> top
        for i in range(bottom - 1, top - 1, -1):
            elements.append(grid[i][right])

        # right -> left
        for j in range(right - 1, left, -1):
            elements.append(grid[top][j])
        
        length = len(elements)
        rot = k % length

        elements = elements[-rot:] + elements[:-rot]
        idx = 0

        # top -> bottom
        for i in range(top, bottom + 1):
            grid[i][left] = elements[idx]
            idx += 1

        # left -> right
        for j in range(left + 1, right + 1):
            grid[bottom][j] = elements[idx]
            idx += 1

        # bottom -> top
        for i in range(bottom - 1, top - 1, -1):
            grid[i][right] = elements[idx]
            idx += 1

        # right -> left
        for j in range(right - 1, left, -1):
            grid[top][j] = elements[idx]
            idx += 1

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rowLen = len(grid)
        colLen = len(grid[0])
        maxLayers = min(rowLen, colLen)//2

        for layer in range(maxLayers):
            top, bottom, left, right = layer, rowLen-layer-1, layer, colLen - layer - 1
            self.rotateEachLevelKtimes(grid, top, bottom, left, right, k)
        return grid