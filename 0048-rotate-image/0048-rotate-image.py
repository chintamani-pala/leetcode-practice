class Solution(object):
    def reverse(self, i, matrix):
        left = 0
        right = len(matrix[i]) - 1
        while( left < right ):
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
        

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length - 1):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        for i in range(length):
            self.reverse(i, matrix)
        return matrix

        