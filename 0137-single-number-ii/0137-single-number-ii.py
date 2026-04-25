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
        # nums.sort()
        # for pointer in range(1, len(nums), 3):
        #     if nums[pointer] != nums[pointer-1]:
        #         return nums[pointer-1]
        # return nums[-1]

        #bit wise with more indepth intution
        once = 0
        twos = 0
        for i in range(len(nums)):
            once =  (once ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~once
        return once 