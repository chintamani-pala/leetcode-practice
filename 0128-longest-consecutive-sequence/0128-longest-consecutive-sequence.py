class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num-1 not in nums_set:
                cnum = num
                temp_res=1
                while cnum + 1 in nums_set:
                    cnum += 1
                    temp_res += 1
                res = max(res, temp_res)
        return res
