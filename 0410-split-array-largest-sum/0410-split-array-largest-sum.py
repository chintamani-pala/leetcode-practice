class Solution(object):
    def noOfpossible(self, nums, val):
        count = 0
        k = 1
        for i in nums:
            if i+count <= val:
                count += i
            else:
                k+=1
                count = i
        
        return k
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>len(nums):
            return -1
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = low+(high-low)//2
            howManyKPossible = self.noOfpossible(nums, mid)
            if howManyKPossible>k:
                low = mid+1
            else:
                high = mid-1
        return low