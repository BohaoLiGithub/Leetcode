class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        list_ = [[0 for _ in range(numRows)] for _ in range(numRows)]
        for idx in range(numRows):
            list_[idx][0] = 1
            list_[0][idx] = 1
        for idx1 in range(1,numRows):
            for idx2 in range(numRows-idx1):
                list_[idx1][idx2] = list_[idx1-1][idx2] + list_[idx1][idx2-1]
        res = []
        res.append([1])
        for idx1 in range(1,numRows):
            tem_list = []
            for idx2 in range(idx1+1):
                tem_list.append(list_[idx2][idx1-idx2])
            res.append(tem_list)
        return res