class Solution(object):
    def checkValidParenthesis(self, str):
        count = 0
        for i in str:
            if i in "(":
                count+=1
            elif i in ")":
                count-=1
        
            if count<0:
                return count
        return count
    def solve(self, curr, n, ans):
        validCount = self.checkValidParenthesis(curr)
        if len(curr) == 2*n:
            if validCount == 0:
                ans.add(curr)
            return
        if validCount < 0 or validCount > n:
            return
        self.solve(curr+"(", n, ans)
        if len(curr)>=1:
            self.solve(curr+")", n, ans)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = set()
        curr = ""
        self.solve(curr,n, ans)
        return list(ans)
        