class Solution(object):
    def kthElementOf2SortedArray(self, a, b, k):
        i=0
        j=0
        while i<len(a) and j<len(b):
            k-=1
            if k==0:
                return a[i] if a[i]<b[j] else b[j]
            if a[i] <= b[j]:
                i+=1
            else:
                j+=1
            
            
        if j>=len(b):
            while i<len(a):
                k-=1
                if k == 0:
                    return a[i]
                i+=1
        if i>=len(a):
            while j<len(b):
                k-=1
                if k==0:
                    return b[j]
                j+=1
        return -1
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if (m+n)%2 == 0:
            firstEle = self.kthElementOf2SortedArray(nums1, nums2, (m+n)//2)
            secondEle = self.kthElementOf2SortedArray(nums1, nums2, ((m+n)//2)+1)
            return float(firstEle+secondEle)/2
        return self.kthElementOf2SortedArray(nums1, nums2, int((m+n)//2)+1)
        