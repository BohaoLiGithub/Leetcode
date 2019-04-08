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
        queue = collections.deque([])
        for idx1 in range(l):
            for idx2 in range(w):
                if matrix[idx1][idx2] == 0:
                    queue.append((idx1,idx2))
                else:
                    matrix[idx1][idx2] = float("inf")
        while queue:
            x,y = queue.popleft()
            newq = collections.deque([])
            newq.append((x-1,y,1))
            newq.append((x,y-1,1))
            newq.append((x+1,y,1))
            newq.append((x,y+1,1))
            while newq:
                a,b,length = newq.popleft()
                if 0<=a<l and 0<=b<w and matrix[a][b] != 0:
                    if length < matrix[a][b]:
                        matrix[a][b] = length
                        newq.append((a-1,b,length+1))
                        newq.append((a,b-1,length+1))
                        newq.append((a+1,b,length+1))
                        newq.append((a,b+1,length+1))
        return matrix