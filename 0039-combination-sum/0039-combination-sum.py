class Solution(object):
    def solve(self, candidates, target,ind, ds , ans):
        if ind == len(candidates):
            if target == 0:
                ans.add(tuple(ds))
            return
        if candidates[ind] <= target:
            ds.append(candidates[ind])
            self.solve(candidates, target-candidates[ind], ind, ds, ans)
            ds.pop()
        self.solve(candidates, target, ind+1, ds, ans)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        self.solve(candidates, target, 0, [], ans)

        return [list(item) for item in ans]