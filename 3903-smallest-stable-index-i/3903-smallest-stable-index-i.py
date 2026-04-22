class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            maxarr = nums[:i+1]
            minarr = nums[i:]
            maxval = max(maxarr)
            minval = min(minarr)
            if maxval - minval <= k:
                return i
        return -1
        