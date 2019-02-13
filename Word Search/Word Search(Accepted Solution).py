class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def exist_helper(board,word,i,j):
            if board[i][j] == word[0]:
                board[i][j] =' '
                if len(word) == 1:
                    return True
                if i >0 and exist_helper(board,word[1:],i - 1, j):
                    return True
                if i < len(board)- 1 and exist_helper(board,word[1:],i+1 ,j):
                    return True
                if j > 0 and exist_helper(board,word[1:],i, j-1):
                    return True
                if j < len(board[0]) - 1 and exist_helper(board,word[1:],i,j+1):
                    return True
                board[i][j] = word[0]
                return False
            else:
                return False
        res = False    
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = exist_helper(board,word,i,j)
                if res:
                    return True
        return res