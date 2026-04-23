class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 1
        suff = 1
        max = min(nums)
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            j = (n - 1) - i
            pre *= nums[i]
            suff *= nums[j]
            temp_max = pre if pre > suff else suff
            max = max if max > temp_max else temp_max
        return max



        