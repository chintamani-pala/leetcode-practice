import math
class Solution(object):
    def sumHour(self, nums, hour):
        return sum(-(-num/hour)for num in nums)
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        while low<=high:
            mid = low + ((high-low)//2)
            requiredTime =  self.sumHour(piles, mid)

            if requiredTime > h:
                low=mid+1
            else:
                high=mid-1
        return low