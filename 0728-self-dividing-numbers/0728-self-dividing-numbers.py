class Solution:
    def check(self, num):
        numStr = str(num)
        if "0" in numStr:
            return False
        for i in numStr:
            if num%int(i) != 0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            if self.check(i):
                ans.append(i)
        return ans