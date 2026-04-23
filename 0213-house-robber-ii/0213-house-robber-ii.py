class Solution(object):
    def rob_single(self, nums):
        dp = [0] *(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            skip = dp[i]
            rubb = nums[i] + dp[i-1]
            dp[i+1] = max(skip, rubb)
        return dp[-1]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):
            return nums[0]
        skip_first = self.rob_single(nums[1:])
        skip_last = self.rob_single(nums[:-1])
        return max(skip_first, skip_last)
        