# Slow
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0
        graph = [[0 for _ in range(n)] for _ in range(n)]
        visited = [0] *n
        res = 0
        for edge in edges:
            a = edge[0]
            b = edge[1]
            graph[a][b] = 1
            graph[b][a] = 1
        for i in range(len(graph)):
            if visited[i] == 1:
                continue
            else:
                self.helper(graph,visited,i)
                res += 1
        return res
                
    def helper(self,G,V,i):
        V[i] = 1
        for j in range(len(G)):
            if (G[i][j] == 0) or (V[j]==1):
                continue
            self.helper(G,V,j)