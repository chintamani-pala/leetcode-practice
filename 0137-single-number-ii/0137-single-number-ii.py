class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #this will work if it numbers are only  positive
        # ans = 0
        # for bitIndex in range(0, 32):
        #     count1 = 0
        #     for item in nums:
        #         if item & (1<<bitIndex):
        #             count1+=1
        #     if count1%3==1:
        #         ans = ans | (1<<bitIndex)
        # return ans

        #use sort and move pointer 
        nums.sort()
        for pointer in range(1, len(nums), 3):
            if nums[pointer] != nums[pointer-1]:
                return nums[pointer-1]
        return nums[-1]