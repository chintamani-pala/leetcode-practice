class Solution(object):
    def countPair(self, arr, low, mid, high):
        count = 0
        j = mid+1
        for i in range(low, mid+1):
            while j<=high and arr[i] > 2*arr[j]:
                j+=1
            count += (j-(mid+1))
        return count

    def merge(self, arr, low, mid, high):
        temp_arr = []
        i = low
        j = mid+1

        while i<=mid and j<=high:
            if arr[i] <= arr[j]:
                temp_arr.append(arr[i])
                i+=1
            else:
                temp_arr.append(arr[j])
                j+=1
        if i>mid:
            while j<=high:
                temp_arr.append(arr[j])
                j+=1
        if j>high:
            while i<=mid:
                temp_arr.append(arr[i])
                i+=1
        for i in range(low, high+1):
            arr[i] = temp_arr[i-low]
    
    
    def mergeSort(self, arr, low, high):
        count = 0
        if low>=high:
            return count
        mid = low+(high-low)//2
        count += self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid+1, high)
        count += self.countPair(arr, low, mid, high)
        self.merge(arr, low, mid, high)
        return count
    
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(nums, 0, len(nums)-1)
#         #ttl
#         # count = 0
#         # for i in range(len(nums)):
#         #     for j in range(i+1, len(nums)):
#         #         if nums[i] > 2*nums[j]:
#         #             count += 1
#         # return count

#         #merge sort

        
                
            