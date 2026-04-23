class Solution(object):
    def bouquestCanForm(self,nums, day, k):
        count = 0
        ans = 0
        for num in nums:
            if num<=day:
                count+=1
            else:
                ans += count//k
                count = 0
    
        if count > 0:
            ans += count//k
        return ans
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low<high:
            mid = low+(high-low)//2
            noOfBouquest = self.bouquestCanForm(bloomDay, mid, k)
            if noOfBouquest < m:
                low = mid+1
            else:
                high = mid
        return low
            
        