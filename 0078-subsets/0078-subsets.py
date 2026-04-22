class Solution(object):
    def solve(self, nums, ds, ind, ans):
        ans.add(tuple(ds))
        if ind == len(nums):
            return
        ds.append(nums[ind])
        self.solve(nums, ds, ind+1, ans)
        ds.pop()
        self.solve(nums, ds, ind+1, ans)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        self.solve(nums, [], 0, ans)
        return [list(item) for item in ans]

        