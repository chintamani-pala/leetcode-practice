class Solution:
    # def calculate(self, num, nums):
    #     num *= -1
    #     sum = 0
    #     #end side
    #     index = 0
    #     for i in nums[num:]:
    #         sum += (index*i)
    #         index+=1
    #     #firstside
    #     if num != 0:
    #         for j in nums[0:num]:
    #             sum += index*j
    #             index+=1
    #     return sum
    # def solve(self, nums):
    #     ans = None
    #     for i in range(len(nums)):
    #         if ans is None:
    #             ans = self.calculate(i, nums)
    #         else:
    #             ans = max(ans, self.calculate(i, nums))
    #     return ans

    #by doing some formulation 
    def solve(self, nums):
        f = sum(i*num for i, num in enumerate(nums))
        totalSum = sum(nums)
        n = len(nums)
        maxValue = f

        for i in range(1, n):
            fn = f + totalSum - (n*nums[n-i])
            f = fn
            maxValue = max(maxValue, fn)
        return maxValue
    def maxRotateFunction(self, nums: List[int]) -> int:
        return self.solve(nums)