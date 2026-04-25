class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if str(x) in str(n) and not str(n).startswith(str(x)):
            return True
        return False