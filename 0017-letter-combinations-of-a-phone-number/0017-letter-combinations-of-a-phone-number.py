class Solution(object):
    def solve(self, idx, digits, phonemap, cs, ans):
        if idx == len(digits):
            ans.add(cs)
            return
        phonestr = phonemap[int(digits[idx])-2]
        for ch in phonestr:
            self.solve(idx+1, digits, phonemap, cs+ch, ans)
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phonemap = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = set()
        self.solve(0, digits, phonemap, "", ans)

        return list(ans)