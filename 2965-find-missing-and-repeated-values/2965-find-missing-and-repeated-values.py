class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        all_items = [num for arr in grid for num in arr]
        n = len(all_items)
        total_sum = sum(all_items)
        set_items = set(all_items)
        distinct_sum = sum(list(set_items))
        actual_sum = (n*(n+1))/2
        return [(total_sum - distinct_sum), (actual_sum - distinct_sum)]
        