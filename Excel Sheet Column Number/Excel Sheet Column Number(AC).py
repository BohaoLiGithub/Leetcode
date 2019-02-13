class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        liststr = list(s)
        res = 0
        a = 0
        for i in range(len(liststr)-1,-1,-1):
            res = res + pow(26,len(liststr) - i - 1) * (ord(liststr[i]) - 64)
        return res