class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        element1 = None
        count1 = 0
        element2 = None
        count2 = 0
        n = len(nums)
        for i in range(n):
            if element1 == nums[i]:
                count1 += 1
            elif element2 == nums[i]:
                count2 += 1
            elif count1 == 0:
                element1 = nums[i]
                count1 += 1
            elif count2 == 0:
                element2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1_valid = 0
        count2_valid = 0
        ans = []
        for num in nums:
            if num == element1:
                count1_valid += 1
            if num == element2:
                count2_valid += 1
        if count1_valid > (n//3):
            ans.append(element1)
        if count2_valid > (n//3):
            ans.append(element2)
        print(count1, element1, count1_valid)
        print(count2, element2, count2_valid)
        return list(ans)