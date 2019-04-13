class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(idx1,idx2):
            if 0<=idx1<l and 0<=idx2<w and grid[idx1][idx2] == 1 and visited[idx1][idx2] == False:
                visited[idx1][idx2] = True
                a1 = dfs(idx1+1,idx2)
                a2 = dfs(idx1,idx2+1)
                a3 = dfs(idx1-1,idx2)
                a4 = dfs(idx1,idx2-1)
                return 1 + a1 + a2 + a3 + a4
            return 0
           
        if not grid:
            return 0
        l = len(grid)
        if type(grid[0]) == list:
            w = len(grid[0])
        visited  = [[False for _ in range(w)] for _ in range(l)]
        res = 0
        for idx1 in range(l):
            for idx2 in range(w):
                if grid[idx1][idx2] == 1:
                    temp = dfs(idx1,idx2)
                    res = max(res,temp)
        return res