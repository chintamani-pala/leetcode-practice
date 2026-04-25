from collections import deque
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adjList = [[] for _ in range(n)]
        for l1, l2 in edges:
            adjList[l1].append(l2)
            adjList[l2].append(l1)

        def isBFSconnected(subsetNodesSet):

            startNode = next(iter(subsetNodesSet))
            visitedNodes = set([startNode])
            queue = deque([startNode])
            
            while len(queue) > 0:
                currentNode = queue.popleft()
                for neibore in adjList[currentNode]:
                    if neibore in subsetNodesSet and neibore not in visitedNodes:
                        visitedNodes.add(neibore)
                        queue.append(neibore)
            return visitedNodes == subsetNodesSet
        
        ans=0
        for maskingValue in range(1, 1 << n):
            subsetNodes =[]
            totalSums = 0
            
            for i in range(n):
                if maskingValue &(1 << i):
                    subsetNodes.append(i)
                    totalSums+= nums[i]
            
            if totalSums % 2 != 0:
                continue
            
            subset_set = set(subsetNodes)
            
            if isBFSconnected(subset_set):
                ans += 1
        
        return ans