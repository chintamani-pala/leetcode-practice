class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sp = 0
        tp = 0
        ss = len(s)
        ts = len(t)

        while(sp < ss and tp < ts):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == ss