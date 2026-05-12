class Solution:
    #binary search on answer
    def isPossible(self, tasks, mid):
        for task in tasks:
            actual = task[0]
            minimum = task[1]
            if minimum > mid:
                return False
            mid -= actual
        return True
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # tasks.sort(key=lambda x: (-x[1], x[0]))
        # initial = tasks[0][1] - tasks[0][0]
        # sum = tasks[0][1]
        # for i in range(1, len(tasks)):
        #     item = tasks[i]
        #     if item[1]>initial:
        #         sum += (item[1] - initial)
        #         initial += (item[1] - initial)
        #         initial -= item[0]
        #     else:
        #         initial -= item[0]
        # return sum

        n = len(tasks)
        tasks.sort(key=lambda x: (-(x[1]-x[0]), -x[1]) )
        left = 0
        right = 10**9
        result = right
        while left<=right:
            mid = left + (right-left)//2
            if self.isPossible(tasks, mid):
                result=mid
                right = mid-1
            else:
                left = mid+1
        return int(result)
