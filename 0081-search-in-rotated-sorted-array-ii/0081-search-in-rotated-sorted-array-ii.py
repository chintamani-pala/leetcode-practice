class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+((high-low)//2)

            if nums[mid] == target:
                return True
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                high -= 1
                low += 1
                continue
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<=nums[mid]:
                    high = mid-1
                else:
                    low  = mid+1
            else:
                if target>=nums[mid] and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False
        