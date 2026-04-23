class Solution(object):
    def find(self, arr, idx, target, sum, combi, ans):
        if target == sum:
            ans.add(tuple(combi))
            return
        if idx == len(arr):
            return
        if sum>target: 
            return
        
        combi.append(arr[idx])
        sum += arr[idx]
        self.find(arr, idx+1, target, sum, combi, ans)
        combi.pop()
        sum -= arr[idx]
        while(idx+1 < len(arr) and arr[idx] == arr[idx+1]):
            idx+=1
        self.find(arr,idx+1, target, sum, combi, ans)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        candidates.sort()
        combi = []
        self.find(candidates, 0, target, 0, combi, ans)
        return list(ans)
