class Solution(object):
    def getPermut(self, nums, idx, ans):
        if idx == len(nums):
            ans.append(nums[:])
            return 
        for i in range(idx, len(nums)):
            nums[idx],nums[i] = nums[i],nums[idx]
            self.getPermut(nums, idx+1, ans)
            nums[i],nums[idx] = nums[idx],nums[i]
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[]
        self.getPermut(nums,0,ans)
        return ans
        