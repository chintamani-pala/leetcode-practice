class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = 1
        ans = ""
        numbers = []
        for i in range(1,n):
            fact*=i
            numbers.append(i)
        numbers.append(n)
        k -= 1
        while True:
            ans += str(numbers[k//fact])
            numbers.pop(k//fact)
            if(len(numbers)==0):
                break
            k = k%fact
            fact = fact // len(numbers)
        return ans 


        