class Solution:
    def reverse(self, matrix, index):
        i= 0 
        j = len(matrix[index])-1
        while i<=j:
            matrix[index][j],  matrix[index][i] = matrix[index][i], matrix[index][j]
            i+=1
            j-=1
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(n):
            self.reverse(matrix, i)
        return matrix 