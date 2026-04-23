class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low + ((high-low)//2)
            if nums[mid] == target:
                low_bound = mid
                higher_bound = mid
                while(low_bound-1 >=0 and nums[low_bound-1] == target):
                    low_bound -= 1
                while (higher_bound+1 < len(nums) and nums[higher_bound+1] == target):
                    higher_bound += 1
                return [low_bound, higher_bound]
            if nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]