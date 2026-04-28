class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr= []
        for items in grid:
            for item in items:
                arr.append(item)
        arr.sort()
        res = 0
        n = len(arr)
        target = arr[n//2]
        for i in range(len(arr)):
            diff = abs(arr[i]- target)
            if diff%x != 0:
                return -1
            
            res += (diff//x)
        return res

