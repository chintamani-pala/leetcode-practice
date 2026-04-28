class Solution:
    def checkString(self, s: str) -> bool:
        firstb = s.find("b")
        if firstb == -1:
            return True
        for i in range(firstb, len(s)):
            if s[i] == "a":
                return False
        return True