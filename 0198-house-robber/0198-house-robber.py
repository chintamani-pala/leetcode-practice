class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1]=nums[0]
        for i in range(1, len(nums)):
            skip_value = dp[i]
            rubb_value = nums[i] + dp[i-1]
            dp[i+1] = max(skip_value, rubb_value)

        return dp[-1] 


        