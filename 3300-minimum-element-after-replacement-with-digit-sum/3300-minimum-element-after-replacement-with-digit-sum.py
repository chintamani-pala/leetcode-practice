class Solution:
    def digitSum(self, num):
        total = 0
        while num>0:
            total += num%10
            num//=10
        return total
    def minElement(self, nums: List[int]) -> int:
        return min([self.digitSum(num) for num in nums])