class Solution(object):
    def __init__(self):
        self.mem = collections.defaultdict()
        self.result = []
        self.mem[''] = True
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        for idx in range(len(s)):
            list_ = []
            right = s[idx:]
            left = s[:idx]
            if right in wordDict:
                list_.append(right)
                self.helper(left,wordDict,list_)
                if not left:
                    self.result.append(right)
        return self.result
                        
    def helper(self,s,wordDict,list_):
        orig_list = list(list_)
        for idx in range(len(s)):
            list_ = list(orig_list)
            right = s[idx:]
            left = s[:idx]
            if right in wordDict:
                list_.append(right)
                self.helper(left,wordDict,list_)
                if left == '':
                    self.result.append(' '.join(list_[::-1]))