class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if total_sum == target:
                        ans_arr = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(ans_arr)
                        k += 1
                        l -= 1
                        while k < l and nums[k-1] == nums[k]:
                            k+=1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif total_sum > target:
                        l -= 1
                    else:
                        k += 1
        return ans  