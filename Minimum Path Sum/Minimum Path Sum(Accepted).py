class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for a in range(1,m):
            grid[a][0] += grid[a-1][0]
        for b in range(1,n):
            grid[0][b] += grid[0][b-1]
        for c in range(1,m):
            for d in range(1,n):
                grid[c][d] += min(grid[c-1][d],grid[c][d-1]) 
        return grid[-1][-1]
        