class Solution(object):
    def countOnes(self, mat, row):
        return sum([1 for i in mat[row] if i == 1])
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        countfq = {}
        for i in range(len(mat)):
            countfq[i] = self.countOnes(mat, i)
        maxCount = max(countfq.values())
        for row, value in countfq.items():
            if value == maxCount:
                return [row, value]
        return []


        