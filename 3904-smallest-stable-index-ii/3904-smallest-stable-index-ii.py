class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxarr = [0 for i in range(len(nums))]
        maxarr[0] = nums[0]
        for i in range(1, len(nums)):
            maxarr[i] = max(maxarr[i-1], nums[i])
        maxval = max(nums)
        minarr = [maxval for i in range(len(nums))]
        minarr[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            minarr[i] = min(minarr[i+1], nums[i])

        for i in range(len(nums)):
            if maxarr[i]-minarr[i] <= k:
                return i
        return -1
        
            
        