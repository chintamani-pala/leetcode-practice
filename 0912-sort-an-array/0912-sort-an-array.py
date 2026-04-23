import random
class Solution(object):
    # def merge(self, nums, low, mid, high):
    #     left = low
    #     right = mid+1
    #     temparr = []
    #     while(left<=mid and right<=high):
    #         if nums[left] < nums[right]:
    #             temparr.append(nums[left])
    #             left += 1
    #         else:
    #             temparr.append(nums[right])
    #             right+=1
    #     while left<=mid:
    #         temparr.append(nums[left])
    #         left+=1
    #     while right<=high:
    #         temparr.append(nums[right])
    #         right+=1
    #     for i in range(low, high+1):
    #         nums[i] = temparr[i-low]
        
    # def mergeSort(self, nums, low, high):
    #     if low>=high:
    #         return
    #     mid = (low+high)/2
    #     self.mergeSort(nums, low, mid)
    #     self.mergeSort(nums, mid+1, high)
    #     self.merge(nums, low, mid, high)
    # def sortAndReturnPartition(self, nums, low, high):
    #     i=low
    #     j=high
    #     pivot_index = random.randint(low, high)#if we choose first element nums[low] if the array is sorted it becomes worst case so the time complexity will be n*n but if we choose last element as pivot and array is reversely sorted that case also the time complexity will be n*n so better to choose a random as a pivot element so the time complexity will be O(n log n)
    #     nums[pivot_index], nums[low] = nums[low], nums[pivot_index]
    #     pivot_element = nums[low]
    #     while(i<j):
    #         while(i<high and nums[i]<=pivot_element):
    #             i+=1
    #         while(j>low and nums[j]>pivot_element):
    #             j-=1
    #         if i<j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #     nums[j], nums[low] = nums[low], nums[j]

    #     return j
        

            
    # def quickSort(self, nums, low, high):
    #     if low>=high:
    #         return
    #     partition_index = self.sortAndReturnPartition(nums, low, high)
    #     self.quickSort(nums, low, partition_index-1)
    #     self.quickSort(nums, partition_index+1, high)

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        
        pivot_index = random.randint(left, right)
        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        pivot = nums[left]

        lessEnd = left
        current = left + 1
        greaterStart = right

        while current <= greaterStart:
            if nums[current] < pivot:
                nums[lessEnd], nums[current] = nums[current], nums[lessEnd]
                lessEnd += 1
                current += 1
            elif nums[current] > pivot:
                nums[current], nums[greaterStart] = nums[greaterStart], nums[current]
                greaterStart -= 1
            else:
                current += 1

        self.quickSort(nums, left, lessEnd - 1)
        self.quickSort(nums, greaterStart + 1, right)
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # self.mergeSort(nums, 0, len(nums)-1)
        # return nums
        self.quickSort(nums, 0, len(nums)-1)
        return nums
        