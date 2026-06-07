class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        obj = {}
        for i in nums:
            obj[i] = obj.get(i, 0)+1
        for i in list(set(nums)):
            if obj.get(i) > k:
                tempAns = [i]*k
            else:
                tempAns = [i]*obj.get(i)
            ans.extend(tempAns)
        return sorted(ans)