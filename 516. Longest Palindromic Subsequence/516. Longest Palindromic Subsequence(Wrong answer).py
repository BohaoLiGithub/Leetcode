class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        if len(s) == 1:
            return 1
        cur = 0
        max_ = 0
        list_ = list(s)
        while cur < len(list_) - 1:
            start = cur
            end = len(list_) - 1
            res = 0
            while start < end:
                #print(start)
                if list_[start] == list_[end]:
                    start += 1
                    end -= 1
                    res += 2
                else:
                    end -= 1
            if start == end:
                res += 1
            max_ = max(max_,res)
            cur += 1
        return max_