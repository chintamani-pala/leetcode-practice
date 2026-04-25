import bisect
class Solution:
    def check(self, arr, k, side, d):
        n = len(arr)
        l = 4*side
        extended = arr + [x + l for x in arr]
        
        for i in range(n):
            count = 1
            pos = extended[i]
            idx = i
            for cnt in range(1, k):
                target = pos+d
                it = bisect.bisect_left(extended, target, idx + 1, i + n)
                if it == i+n:
                    count = -1
                    break

                idx = it
                pos = extended[idx]
                count+=1
            if count == k and (extended[i] + l -pos) >= d:
                return True
        return False 
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr =[]
        for item in points:
            x, y = item
            if y==0:
                arr.append(x)
            elif x == side:
                arr.append(side+y)
            elif y==side:
                arr.append(2*side+(side-x))
            else:
                arr.append(3*side+(side-y))
        
        arr.sort()

        low = 0
        high = 2*side
        ans = 0

        while low<=high:
            mid = low+(high-low)//2
            if self.check(arr, k, side, mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans