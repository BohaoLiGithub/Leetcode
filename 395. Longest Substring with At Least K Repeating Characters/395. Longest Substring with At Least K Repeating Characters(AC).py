class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        counter = collections.Counter(s)
        temp = []
        for i in counter.items():
            if i[1] < k:
                temp.append(i[0])
        if len(temp) == 0:
            return len(s)
        for j in range(len(temp)):
            s = s.replace(temp[j],' ')
        temp_ = s.split(' ')
        result = 0
        for p in range(len(temp_)):
            result = max(result,self.longestSubstring(temp_[p],k))
        return result