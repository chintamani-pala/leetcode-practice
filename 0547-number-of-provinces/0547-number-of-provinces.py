class Solution(object):
    def dfs(self, adj, node, visited):
        visited[node]=1
        for item in adj[node]:
            if not visited[item]:
                self.dfs(adj, item, visited)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        adj = [[] for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
                    # adj[j].append(i)
        visited = [0]*len(adj)
        count = 0
        for i in range(len(visited)):
            if not visited[i]:
                count += 1
                self.dfs(adj, i, visited) 
        return count