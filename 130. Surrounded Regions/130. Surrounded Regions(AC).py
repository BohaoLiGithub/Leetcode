class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        queue = collections.deque()
        m = len(board)
        if m:
            n = len(board[0])
        for idx1 in range(m):
            for idx2 in range(n):
                if (idx1 in [0,m-1] or idx2 in [0,n-1]) and board[idx1][idx2] == 'O':
                    queue.append((idx1,idx2))
        while queue:
            idx1,idx2 = queue.popleft()
            if 0<=idx1<m and 0<=idx2<n and board[idx1][idx2] == 'O':
                queue.append((idx1-1,idx2))
                queue.append((idx1+1,idx2))
                queue.append((idx1,idx2-1))
                queue.append((idx1,idx2+1))
                board[idx1][idx2] = 'K'
                
        for idx1 in range(m):
            for idx2 in range(n):
                if board[idx1][idx2] == 'K':
                    board[idx1][idx2] = 'O'
                elif board[idx1][idx2] == 'O':
                    board[idx1][idx2] = 'X'