class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        if s in wordDict:
            return True
        flag = False
        for idx in range(1,len(s)):
            #print(s[:idx])
            if s[:idx] in wordDict:
                res = self.wordBreak(s[idx:],wordDict)
                if res:
                    flag = True
                #print(res)
        return flag
        