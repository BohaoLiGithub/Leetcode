import heapq
import functools

@functools.total_ordering
class Element(object):
    def __init__(self,count,word):
        self.count = count
        self.word = word
    def __lt__(self,other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    def __eq__(self,other):
        return self.count == other.count and self.word == other.word
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_freq = collections.Counter(words)
        res = []
        heapq.heapify(res)
        for word, count in word_freq.items():
            heapq.heappush(res,(Element(count,word),word))
            if len(res) > k:
                heapq.heappop(res)
        res_ = []
        for _ in range(k):
            res_.append(heapq.heappop(res)[1])
        return res_[::-1]