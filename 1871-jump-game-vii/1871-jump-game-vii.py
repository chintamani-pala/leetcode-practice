from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        t = [0]*n
        #t[i] > 0: possible to reach i
        ## == 0: not possible to reach i
        t[0] = 1
        count = 0
        for j in range(1, n):
            if j-minJump >= 0:
                count += t[j-minJump]
            if j-maxJump-1 >= 0:
                count -= t[j-maxJump-1]
            
            if count > 0 and s[j] == '0':
                t[j] = 1
        return t[n-1]>0 

