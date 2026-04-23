class Solution(object):
    def findRow(self, n):
        ans = 1
        res = []
        res.append(ans)
        if(n<=1):
           return res 
        for i in range(1, n-1):
            ans = ans * (n-i)
            ans/=i
            res.append(ans)
        res.append(1)
        return res

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows+1):
            res.append(self.findRow(i))
        return res
        