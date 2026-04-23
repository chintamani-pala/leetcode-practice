import math
class Solution(object):
    def isPrime(self, num):
        if num<=1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if i%2==0:
                if not self.isPrime(num):
                    while not self.isPrime(num):
                        sum += 1
                        num += 1
            
            else:
                if self.isPrime(num):
                    while self.isPrime(num):
                        sum += 1
                        num += 1
        return sum
                