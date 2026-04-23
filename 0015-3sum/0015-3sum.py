class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        i = 0
        nums.sort()
        while i < len(nums)-1:
            j = i + 1
            k = len(nums)-1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum == 0:
                    ans_eles = [nums[i], nums[j], nums[k]]
                    ans.add(tuple(ans_eles))
                    j += 1
                    k -= 1
                elif total_sum > 0:
                    k -= 1
                else:
                    j += 1
                    while j > 0 and j < len(nums) - 1 and nums[j] == nums[j-1]:
                        j += 1
                    while k > 0 and k < len(nums)-1 and nums[k+1] == nums[k]:
                        k -= 1
            i += 1   
            while i < len(nums)-1 and nums[i] == nums[i-1]:
                i += 1
        return list(ans)


