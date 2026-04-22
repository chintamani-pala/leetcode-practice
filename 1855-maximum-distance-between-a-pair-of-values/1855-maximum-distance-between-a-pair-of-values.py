class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        #time complexity: O(n^2)
        #space complexity: O(1)
        #this will give TLE
        # maxdistance = 0
        # for i in range(len(nums1)):
        #     for j in range(i, len(nums2)):
        #         if nums1[i]<=nums2[j]:
        #             maxdistance = max(maxdistance, abs(i-j))
        # return maxdistance

        # maxdistance = 0
        # for i in range(len(nums1)):
        #     for j in range(i, len(nums2)):
        #         if nums1[i]<=nums2[j]:
        #             maxdistance = max(maxdistance, abs(i-j))
        #         #here the else observation was if a nums1[i] is grater then all the items of nums2 will be grater because nums2 is sortedin non desending manner
        #         else:
        #             break
        # return maxdistance

        #two pointer approch
        i, j = 0, 0
        maxd = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                maxd = max(maxd, j-i)
                j+=1
            else:
                i+=1
        return maxd


        