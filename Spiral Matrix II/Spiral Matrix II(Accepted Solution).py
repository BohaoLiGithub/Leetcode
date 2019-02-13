class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def recursivehelper(matrix,row_start,row_end,col_start,col_end,start_num):
            value = start_num
            if row_start > row_end or col_start > col_end:
                return None
            elif row_start == row_end and col_start == col_end:
                matrix[row_start][col_start] = start_num
            elif row_start == row_end and col_start <= col_end:
                for i in range(col_start,col_end+1):
                    matrix[row_start][i] = value
                    value += 1
            elif row_start < row_end and col_start == col_end:
                for j in range(row_start,row_end+1):
                    matrix[j][col_start] = value
                    value += 1
            else:
                for i in range(col_start,col_end):
                    matrix[row_start][i] = value
                    value += 1
                for j in range(row_start,row_end):
                    matrix[j][col_end] = value
                    value += 1
                for m in reversed(range(col_start+1,col_end+1)):
                    matrix[row_end][m] = value
                    value += 1
                for n in reversed(range(row_start+1,row_end+1)):
                    matrix[n][col_start] = value
                    value += 1
            recursivehelper(matrix,row_start+1,row_end-1,col_start+1,col_end-1,value)
        if n == 0:
            return None
        matrix = [[0 for i in range(n)] for j in range(n)]
        recursivehelper(matrix,0,n-1,0,n-1,1)
        return matrix