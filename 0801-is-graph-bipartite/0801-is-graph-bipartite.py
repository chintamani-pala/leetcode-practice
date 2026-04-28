class Solution:
    def dfs(self,node, col, color, graph):
        color[node] = col
        for i in graph[node]:
            if color[i] == -1:
                if(self.dfs(i, not col, color, graph) == False):
                    return False
            elif color[i] == col:
                return False
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                if self.dfs(i, 0, color, graph) == False:
                    return False
        return True