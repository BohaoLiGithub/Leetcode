class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic_ = {}
        self.length = len(words)
        for idx,val in enumerate(words):
            self.dic_[val] = self.dic_.get(val,[]) + [idx]
        
        ##for idx in range(len(words)):
            ##if words[idx] not in self.dic_.keys():
                ##self.dic_[words[idx]] = [idx]
            ##else:
                ##self.dic_[words[idx]].append(idx)
       
        
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = self.dic_[word1]
        w2 = self.dic_[word2]
        i,j = 0,0
        min_ = self.length
        while i < len(w1) and j < len(w2):
            min_ = min(min_,abs(w1[i] - w2[j]))
            if w1[i] < w2[j]:
                i+=1
            elif w1[i] > w2[j]:
                j+=1
            else:
                return 0
        return min_
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)