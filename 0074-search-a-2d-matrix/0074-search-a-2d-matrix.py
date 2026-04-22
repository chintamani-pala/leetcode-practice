class Solution(object):
    def binarySearch(self, arr, target):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid] == target:
                return True
            if arr[mid]> target:
                high= mid-1
            else:
                low=mid+1
        return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[0]<=target and i[-1]>=target:
                return self.binarySearch(i, target)
        return False
        