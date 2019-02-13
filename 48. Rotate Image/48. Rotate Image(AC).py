#http://javabypatel.blogspot.com/2016/11/rotate-matrix-by-90-degrees-inplace.html
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix) - 1
        for i in range(0,length/2+1,1):
            for j in range(i,length-i,1):
                a = matrix[i][j]
                c = matrix[length-j][i]
                b = matrix[j][length-i]
                d = matrix[length-i][length-j]
                
                matrix[i][j] = c
                matrix[length-j][i] = d
                matrix[j][length-i] = a
                matrix[length-i][length-j] = b