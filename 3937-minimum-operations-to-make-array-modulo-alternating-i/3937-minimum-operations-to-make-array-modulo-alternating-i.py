class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        copyNum = nums[:]
        n=len(nums)
        reminders = [num%k for num in nums]

        ans = float('inf')
        for x in range(k):
            for y in range(k):
                if x==y:
                    continue
                totalCost = 0
                for i in range(n):
                    currentRem = reminders[i]
                    target = x if i%2==0 else y

                    diff = abs(currentRem-target)
                    cost = min(diff, k-diff)

                    totalCost += cost

                ans = min(ans, totalCost)
        return ans
        