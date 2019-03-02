class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x = len(board)
        y = len(board[0]) if x > 0 else 0
        res = 0
        visited = [[0 for _ in xrange(y)] for _ in xrange(x)]
        
        def DFS(x,y,i,j):
            if not (0<=i < x and 0<=j < y):
                return
            if board[i][j] == 'X' and visited[i][j] == 0:
                visited[i][j] = 1
                DFS(x,y,i+1,j)
                DFS(x,y,i,j+1)
            else:
                return  
        for i in range(x): # raw
            for j in range(y): # col
                if board[i][j] == 'X' and visited[i][j] == 0:
                    visited[i][j] = 1
                    res += 1
                    DFS(x,y,i+1,j)
                    DFS(x,y,i,j+1)
        return res