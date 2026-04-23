class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum  = min(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maximum = max(sum, maximum)
            if sum < 0:
                sum  = 0
        return maximum