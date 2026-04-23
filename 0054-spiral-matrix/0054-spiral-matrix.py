class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        sc = 0
        sr = 0
        ec = n-1
        er = m-1
        result = []
        while sr <= er and sc <= ec:
            i = sc
            while(i<=ec):
                result.append(matrix[sr][i])
                i+=1
            sr += 1
            
            i  = sr
            while i <= er:
                result.append(matrix[i][ec])
                i += 1
            ec -= 1

            if sr <= er:
                i = ec
                while i >= sc:
                    result.append(matrix[er][i])
                    i -= 1
            er -= 1

            if sc <= ec:
                i = er
                while i >= sr:
                    result.append(matrix[i][sc])
                    i -= 1
            sc += 1
        return result

        