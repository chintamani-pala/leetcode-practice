class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        count = 0
        map = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if(map.get(sum%k, None)):
                count += map.get(sum%k)
            map[sum%k] = map.get(sum%k,0)+1
        return count
        