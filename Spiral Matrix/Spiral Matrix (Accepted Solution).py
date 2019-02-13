# DP solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def recursivehelper(matrix,result,row_start,row_end,col_start,col_end):
            if row_end < row_start or col_end < col_start:
                return None
            elif row_end == row_start and col_end == col_start:
                result.append(matrix[row_start][col_start])
            elif col_end != col_start and row_start == row_end:
                for i in range(col_start,col_end+1):
                    result.append(matrix[row_start][i])
            elif row_start != row_end and col_end == col_start:
                for i in range(row_start,row_end+1):
                    result.append(matrix[i][col_end])
            else:
                for i in range(col_start,col_end):
                    result.append(matrix[row_start][i])
                for j in range(row_start,row_end):
                    result.append(matrix[j][col_end])
                for m in reversed(range(col_start+1,col_end+1)):
                    result.append(matrix[row_end][m])
                for n in reversed(range(row_start+1,row_end+1)):
                    result.append(matrix[n][col_start])
            recursivehelper(matrix,result,row_start+1,row_end-1,col_start+1,col_end-1)
        res = []
        if matrix == []:
            return res
        recursivehelper(matrix,res,0,len(matrix)-1,0,len(matrix[0])-1)
        return res