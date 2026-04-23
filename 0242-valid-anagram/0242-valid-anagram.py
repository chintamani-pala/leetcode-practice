class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False

        # dict={}
        # for ch in s:
        #     if ch in dict:
        #         dict[ch] += 1
        #     else:
        #         dict[ch] = 1
        
        # for ch in t:
        #     if ch not in dict or dict[ch] == 0:
        #         return False
        #     else:
        #         dict[ch] -= 1

        # return True
        return sorted(s) == sorted(t)
        