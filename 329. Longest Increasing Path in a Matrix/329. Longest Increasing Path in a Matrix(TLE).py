class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        l = len(matrix)
        max_ = 1
        if type(matrix[0]) == list:
            w = len(matrix[0])
        for idx1 in range(l):
            for idx2 in range(w):
                stack = [(idx1,idx2,matrix[idx1][idx2],[matrix[idx1][idx2]])]
                while stack:
                    x,y,val,seq = stack.pop()
                    for m,n in (x,y+1),(x+1,y),(x,y-1),(x-1,y):
                        if 0<=m<l and 0<=n<w and matrix[m][n]>val:
                            stack.append((m,n,matrix[m][n],seq+[matrix[m][n]]))
                        elif 0<=m<l and 0<=n<w and matrix[m][n] <= val:
                            max_ = max(max_,len(seq))
        return max_
                    