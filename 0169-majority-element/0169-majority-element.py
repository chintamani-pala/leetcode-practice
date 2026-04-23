class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele = None
        count = 0
        for num in nums:
            if ele == None or count == 0:
                ele = num
                count = 1
            
            elif ele == num:
                count+=1
            else:
                count-=1
            
            
            # if count == 0:
            #     ele = None
            # else:
            #     ele = num
        return ele
            

        