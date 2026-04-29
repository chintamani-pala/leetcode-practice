class Solution:
    def dfs(self, graph, node, col, color):
        color[node]=col
        for i in graph[node]:
            if color[i] == -1:
                if self.dfs(graph, i, not col, color) == False:
                    return False
            elif color[i] == col:
                return False
        return True
                
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i]  == -1:
                if self.dfs(graph, i, 0, color) == False:
                    return False
        return True
