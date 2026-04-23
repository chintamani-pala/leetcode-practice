class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(matrix)):
            count = 0
            for j in range(0, len(matrix)):
                if matrix[j][i] == 1:
                    count+=1
            ans.append(count)
        return ans
        