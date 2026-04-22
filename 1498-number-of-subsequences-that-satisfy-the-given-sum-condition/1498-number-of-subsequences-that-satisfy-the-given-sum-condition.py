class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        MOD = 10**9+7
        l = 0
        r = len(nums)-1
        ans = 0
        # power = [1] * len(nums)
        # for i in range(1,len(nums)):
        #     power[i] = (power[i-1]*2)%MOD
        while l<=r:
            if nums[l]+nums[r] > target:
                r-=1
            else:
                ans = (ans + 2**(r-l)) % MOD
                # ans = (ans + power[r-l]) % MOD
                l+=1
        return ans


        