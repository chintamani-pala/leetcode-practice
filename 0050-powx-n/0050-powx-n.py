class Solution(object):
    def getPower(self, x, n):
        if n == 0:
            return 1
        half = self.getPower(x, n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>=0:
            return self.getPower(x,n)
        return 1.0/self.getPower(x,-1*n)
        
        