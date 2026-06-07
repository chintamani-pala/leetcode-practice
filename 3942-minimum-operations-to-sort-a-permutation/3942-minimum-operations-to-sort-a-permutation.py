class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #check increasing
        n=len(nums)
        isIncreasing = True
        zeroIndex = nums.index(0)
        indMax = nums.index(n-1)
        for i in range(n):
            nxt = (i+1)%n
            if nums[nxt] != (nums[i]+1)%n:
                isIncreasing = False
                break
        ans = float('inf')
        if isIncreasing:
            ans = min(ans, zeroIndex)
            rotation = (n-zeroIndex)%n
            ans = min(ans, 2+rotation)

        #decreasing side
        isDecresing = True
        for i in range(n):
            nxt = (i+1)%n
            if nums[nxt] != (nums[i]-1)%n:
                isDecresing = False
                break

        if isDecresing:            
            ans = min(ans, indMax+1)
            ans = min(ans, 1+(n-1-zeroIndex))

        return ans if ans!=float('inf') else -1

        
                