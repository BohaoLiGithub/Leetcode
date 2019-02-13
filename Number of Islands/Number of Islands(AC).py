class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def markIsland(i,j):
            #print('i:'+str(i)+' j:'+ str(j))
            if (i<0 or i>row-1 or j<0 or j>col-1 or (grid[i][j] != '1')):
                return
            grid[i][j] = '0'
            markIsland(i-1,j)
            markIsland(i+1,j)
            markIsland(i,j-1)
            markIsland(i,j+1)
        count = 0
        if grid is None:
            return 0
        row = len(grid)
        if row:
            col = len(grid[0])
        else:
            col = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    #print("dadf")
                    count+=1
                    markIsland(i,j)
        return count