class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = {0:1}
        sum = 0
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            res += map.get(sum-k, 0)
            map[sum] = map.get(sum, 0) + 1
        return res
        