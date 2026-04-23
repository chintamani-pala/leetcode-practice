class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low<=high:
            mid = low+(high-low)//2
            if mid*mid > x:
                high = mid-1
            else:
                ans = mid
                low = mid+1
        return ans
        