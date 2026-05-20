class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0]
        obj = {}
        for i in range(0, len(A)):
            if A[i] == B[i]:
                ans.append(ans[-1]+1)
            else:
                ans.append(ans[-1]+obj.get(A[i], 0)+obj.get(B[i], 0))
            obj[A[i]] = obj.get(A[i], 0)+1
            obj[B[i]] = obj.get(B[i], 0)+1
        return ans[1:]
