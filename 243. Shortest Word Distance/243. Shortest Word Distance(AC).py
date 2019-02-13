class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size_ = len(words)
        index1, index2 = size_, size_
        res = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
                res = min(res,abs(index1-index2))
            elif words[i] == word2:
                index2 = i
                res = min(res,abs(index1-index2))
        return res