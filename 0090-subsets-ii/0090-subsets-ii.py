class Solution(object):
    def solve(self, nums, ind, ds, ans):
        ans.add(tuple(ds))
        if ind == len(nums):
            return
        ds.append(nums[ind])
        self.solve(nums, ind+1, ds, ans)
        ds.pop()
        self.solve(nums, ind+1, ds, ans)
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        nums.sort()
        self.solve(nums, 0, [], ans)
        return [list(item) for item in ans]