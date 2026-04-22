class Solution(object):
    def solve(self, nums, idx, ds, k, target, ans):
        if len(ds) == k:
            if target == 0:
                ans.add(tuple(ds))
            return
        if idx >= len(nums):
            return
        ds.append(nums[idx])
        self.solve(nums, idx+1, ds, k, target-nums[idx], ans)
        ds.pop()
        self.solve(nums, idx+1, ds, k, target, ans)
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,10)]
        ans = set()
        self.solve(nums, 0, [], k, n, ans)
        return [list(item) for item in ans]