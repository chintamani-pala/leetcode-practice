class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        preMax = [nums[0]]
        for i in range(1, len(nums)):
            preMax.append(max(preMax[i-1], nums[i]))
        suff = [float('inf')]*len(nums)
        suff[-1] =  nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = min(nums[i], suff[i+1])
        minVal = min(nums)
        ans = [minVal]*len(nums)
        ans[-1] = preMax[-1]
        for i in range(len(nums)-2,-1, -1):
            if preMax[i]>suff[i+1]:
                ans[i] = ans[i+1]
            else:
                ans[i] = preMax[i]
        return ans