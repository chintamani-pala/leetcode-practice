import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_letter(c):
            return re.match(r"[a-z0-9]", c)

        s = s.lower()
        cleaned = ""
        for char in s:
            if is_letter(char):
                cleaned += char
        reversed_str = cleaned[::-1]

        return cleaned == reversed_str
