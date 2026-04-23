from typing import List
from functools import cmp_to_key

class Solution:
    def maxValue(self, nums1: List[int], nums0: List[int]) -> int:
        MOD = 10**9 + 7

        def generateRLEPattern(a1, z1, a2, z2):
            block = [0] * 4
            total = 1
            block[0] = a1

            if z1 > 0:
                block[1] = z1
                total = 2

                if a2 > 0:
                    block[2] = a2
                    total = 3

                    if z2 > 0:
                        block[3] = z2
                        total = 4
                else:
                    if z2 > 0:
                        block[1] += z2
            else:
                block[0] += a2
                if z2 > 0:
                    block[1] = z2
                    total = 2

            return block, total

        def isGreater(A, B):
            a1, z1 = A
            a2, z2 = B

            AB, tAB = generateRLEPattern(a1, z1, a2, z2)
            BA, tBA = generateRLEPattern(a2, z2, a1, z1)

            for i in range(min(tAB, tBA)):
                if AB[i] != BA[i]:
                    if i % 2 == 0:  # ones block
                        return AB[i] > BA[i]
                    else:           # zeros block
                        return AB[i] < BA[i]
            return False

        def comparator(a, b):
            if isGreater(a, b):
                return -1
            if isGreater(b, a):
                return 1
            return 0

        def mod_pow(base, exp):
            res = 1
            base %= MOD
            while exp:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp //= 2
            return res

        segments = list(zip(nums1, nums0))
        segments.sort(key=cmp_to_key(comparator))

        ans = 0

        for ones, zeros in segments:
            length = ones + zeros

            ans = (ans * mod_pow(2, length)) % MOD

            val = ((mod_pow(2, ones) - 1 + MOD) % MOD) * mod_pow(2, zeros) % MOD
            ans = (ans + val) % MOD

        return ans