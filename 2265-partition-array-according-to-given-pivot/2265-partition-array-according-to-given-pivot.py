class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        pivotCount = 0
        for item in nums:
            if item == pivot:
                pivotCount+=1
                continue
            if item<pivot:
                less.append(item)
            if item>pivot:
                more.append(item)
        for i in range(pivotCount):
            less.append(pivot)
        less.extend(more)
        return less