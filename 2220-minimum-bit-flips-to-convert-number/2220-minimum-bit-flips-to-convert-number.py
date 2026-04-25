class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #to identify how many bits are changed
        xor = start ^ goal
        ans = 0

        #Counting number of set bits
        while xor > 0:
            ans += xor & 1
            xor >>= 1
        return ans