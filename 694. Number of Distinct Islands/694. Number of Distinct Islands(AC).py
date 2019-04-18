class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(r,c,r0,c0):
            if 0<=r<l and 0<=c<w and grid[r][c] == 1 and not visited[r][c]:
                shape.add((r-r0,c-c0))
                visited[r][c] = True
                for m,n in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                    dfs(m,n,r0,c0)
        
        if not grid:
            return -1
        l = len(grid)
        w = len(grid[0])
        res = set()
        visited = [[False for _ in range(w)] for _ in range(l)]
        for idx1 in range(l):
            for idx2 in range(w):
                shape = set()
                if grid[idx1][idx2] == 1 and not visited[idx1][idx2]:
                    #res += 1
                    dfs(idx1,idx2,idx1,idx2)
                    #print(shape)
                    if shape not in res:
                        res.add(frozenset(shape))
        return len(res)