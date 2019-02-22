#DFS
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0
        res = 0
        visited = [0] * len(M)
        for i in range(len(M)):
            if visited[i] == 1:
                continue
            self.helper(M,i,visited)
            res += 1
        return res
            
    def helper(self,M,i,V):
        V[i] = 1
        for j in range(len(M)):
            if (M[i][j] == 0) or (V[j] == 1):
                continue
            self.helper(M,j,V)