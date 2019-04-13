class Solution(object):
    def __init__(self):
        self.mem = {string:bool}
        self. mem[''] = True
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in self.mem:
            return self.mem[s]

        for idx in range(len(s)):
            if s[idx:] in self.mem: ## in mem
                if self.mem[s[idx:]]:
                    left = s[:idx]
                    res = self.wordBreak(left,wordDict)
                    if res:
                        return True
            else:  ## not in mem
                if s[idx:] in wordDict:
                    self.mem[s[idx:]] = True
                    left = s[:idx]
                    res = self.wordBreak(left,wordDict)
                    if res:
                        return True
                else:
                    self.mem[s[idx:]] = False
        return False