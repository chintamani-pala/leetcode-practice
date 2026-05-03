class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s is None or goal is None or len(s)  != len(goal) :
            return False
        concatString = s+s
        return True if concatString.find(goal) != -1 else False

