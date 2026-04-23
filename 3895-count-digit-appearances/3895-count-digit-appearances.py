class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        finalNum = ""
        for num in nums:
            finalNum += str(num)
        count = 0
        for num in finalNum:
            if num == str(digit):
                count += 1
        return count
        