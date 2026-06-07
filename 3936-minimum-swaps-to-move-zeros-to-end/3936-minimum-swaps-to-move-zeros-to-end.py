class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count = 0
        i = 0
        j=len(nums)-1
        while i<j:
            if nums[j] != 0 and nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                count+=1
            while j>=0 and nums[j] == 0:
                j-=1
            while i<len(nums)-1 and nums[i] != 0:
                i+=1
        
        return count
        
                