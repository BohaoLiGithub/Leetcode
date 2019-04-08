class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return [[]]
        l = len(matrix)
        if type(matrix[0]) == list:
            w = len(matrix[0])
        queue = []
        for idx1 in range(l):
            for idx2 in range(w):
                if matrix[idx1][idx2] == 0:
                    queue.append((idx1,idx2))
                else:
                    matrix[idx1][idx2] = float("inf")
        for x,y in queue:
            for r,c in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]:
                z = matrix[x][y] + 1
                if 0 <= r < l and 0 <= c < w and matrix[r][c] > z:
                    matrix[r][c] = z
                    queue.append((r,c))
        return matrix