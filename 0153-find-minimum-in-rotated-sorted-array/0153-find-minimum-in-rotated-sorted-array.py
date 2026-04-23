class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums)
        low = 0
        high = len(nums)-1
        ans = nums[0]
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]<=nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
            else:
                ans = min(ans, nums[low])
                low = mid+1
        return ans


