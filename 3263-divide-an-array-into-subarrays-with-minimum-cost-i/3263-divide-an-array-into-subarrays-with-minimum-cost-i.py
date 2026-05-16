class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        remaining = nums[1:]
        remaining.sort()
        return nums[0] + remaining[0] + remaining[1]