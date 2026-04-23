class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in seen:
                res.append(nums[i])
                seen[nums[i]] += 1 
            else:
                seen[nums[i]] = 1
        return res


        