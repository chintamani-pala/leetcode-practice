class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        breakpoint = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1] :
                breakpoint = i
                break
        if breakpoint == -1:
            nums.reverse()
            
        nums[breakpoint+1:] = sorted(nums[breakpoint+1:])

        for i in range(breakpoint+1, len(nums)):
            if nums[i] > nums[breakpoint]:
                nums[i], nums[breakpoint] = nums[breakpoint], nums[i]
                break
        
        


    