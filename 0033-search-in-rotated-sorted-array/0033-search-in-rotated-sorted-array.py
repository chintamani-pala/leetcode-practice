class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                return mid
            #sorted part
            if nums[low]<=nums[mid]:
                #checking the target value present in between low and mid pointer
                if target>=nums[low] and target<=nums[mid]:
                    high = mid - 1
                else:
                    #if target value not present inside low and mid pointer
                    low = mid + 1
            #unsorted part
            else:
                #checking the target value present in between mid and high pointer
                if target>=nums[mid] and target<=nums[high]:
                    low = mid + 1
                else:
                    #if target value not present inside mid and high pointer
                    high = mid - 1
        return -1 


