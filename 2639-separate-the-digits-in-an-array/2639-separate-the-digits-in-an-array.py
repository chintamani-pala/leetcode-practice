class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            j = str(i)
            for k in j:
                result.append(int(k))
        return result