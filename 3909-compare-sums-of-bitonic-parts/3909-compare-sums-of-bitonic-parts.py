class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        ascendingSideSum = nums[0]
        descendingSideSum = 0
        currentElement = nums[0]
        isPeakFound = False
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                ascendingSideSum += nums[i]
            else:
                if not isPeakFound:
                    descendingSideSum += nums[i-1]
                    isPeakFound = True
                descendingSideSum += nums[i]
        if ascendingSideSum>descendingSideSum:
            return 0
        if ascendingSideSum<descendingSideSum:
            return 1
        return -1
                
        