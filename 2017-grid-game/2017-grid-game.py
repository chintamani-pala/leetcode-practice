class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        upperSum = sum(grid[0])
        lowerSum = 0
        res = float("inf")
        for i in range(len(grid[0])):
            upperSum -= grid[0][i]
            res = min(res, max(upperSum, lowerSum))
            lowerSum += grid[1][i]
        return int(res)