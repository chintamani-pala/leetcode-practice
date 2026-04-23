class Solution(object):
    def isPalin(self, s):
        # Helper function to check if a string is a palindrome
        return s == s[::-1]
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def validPartition(s, parti, ans):
            # Base case: if the string is empty, add the current partition to the results
            if len(s) == 0:
                ans.append(parti[:])  # Append a copy of the current partition
                return
            
            # Iterate over all possible prefixes of the string
            for i in range(len(s)):
                subStr = s[:i+1]  # Current prefix
                if self.isPalin(subStr):  # Check if the prefix is a palindrome
                    parti.append(subStr)  # Choose the current prefix
                    validPartition(s[i+1:], parti, ans)  # Explore the remaining string
                    parti.pop()  # Backtrack
        
        ans = []
        validPartition(s, [], ans)
        return ans
