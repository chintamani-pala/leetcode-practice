class Solution:
    def check(self, index, d, arr, dp):
        res = 1
        if dp[index]!=-1:
            return dp[index]
        #left check
        for j in range(index-1, max(-1, index-d-1), -1):
            if arr[j] >= arr[index]:
                break
            res = max(res, 1+self.check(j, d, arr, dp))
        #right check
        for j in range(index+1, min(len(arr), index+d+1)):
            if arr[j] >= arr[index]:
                break
            res = max(res, 1+self.check(j, d, arr, dp))
        dp[index] = res
        return res
    def maxJumps(self, arr: List[int], d: int) -> int:
        ans = 1
        n = len(arr)
        dp = [-1]*n
        for i in range(n):
            ans = max(ans, self.check(i, d, arr, dp))
        return ans