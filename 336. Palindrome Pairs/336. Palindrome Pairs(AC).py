class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {}
        res = set()
        for i in range(len(words)):
            dic[words[i]] = i
        for idx, word in enumerate(words):
            if word and self.isPalindrome(word) and "" in dic:
                eidx = dic[""]
                res.add((idx,eidx))
                res.add((eidx,idx))
            rword = word[::-1]
            if word and rword in dic:
                ridx = dic[rword]
                if ridx != idx:
                    res.add((idx,ridx))
                    res.add((ridx,idx))
            
            for j in range(1,len(word)):
                left,right = word[:j],word[j:]
                rleft,rright = left[::-1],right[::-1]
                if self.isPalindrome(left) and rright in dic:
                    ridx = dic[rright]
                    res.add((ridx,idx))
                if self.isPalindrome(right) and rleft in dic:
                    lidx = dic[rleft]
                    res.add((idx,lidx))
        return list(res)
            
        
    def isPalindrome(self,word):
        length = len(word)
        for i in range(length/2):
            if word[i] != word[length-1-i]:
                return False
        return True