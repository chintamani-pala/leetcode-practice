class Solution(object):
    def findSum(self,nums,devisor):
        return sum(-(-num//devisor) for num in nums)
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        ans = 1
        while low<high:
            mid = low+(high-low)//2
            total = self.findSum(nums, mid)
            
            if total>threshold:
                low=mid+1
            else:
                high = mid
        return low