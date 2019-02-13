class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        matrix = [[0 for i in range(n) ] for j in range(m)]
        for c in range(m):
            matrix[c][0] = 1
        for d in range(n):
            matrix[0][d] = 1
        for a in range(1,m):
            for b in range(1,n):
                matrix[a][b] = matrix[a-1][b] + matrix[a][b-1]
        return matrix[-1][-1]