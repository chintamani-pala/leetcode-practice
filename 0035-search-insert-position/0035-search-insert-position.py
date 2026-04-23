class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            if low == high:
                if nums[low] < target:
                    return low+1
                else:
                    return low
            mid = low+((high-low)//2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] < target:
                    return mid-1
                high = mid-1
            else:
                if nums[mid+1]> target:
                    return mid+1 
                low = mid + 1
        return 0