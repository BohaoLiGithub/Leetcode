class Solution(object):
    def __init__(self):
        self.mem = collections.defaultdict(list)
        self.result = []
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s in self.mem:
            return self.mem[s]
        ans = []
        if s in wordDict:
            ans.append(s)
        for idx in range(len(s)):
            right = s[idx:]
            left = s[:idx]
            if right not in wordDict:
                continue
            left_ans = self.append(self.wordBreak(left,wordDict),right) ##list
            for var in left_ans:
                ans.append(var)
        self.mem[s] = ans
        return self.mem[s]
                        
    def append(self,left_list,right):
        res = []
        for idx in range(len(left_list)):
            res.append(left_list[idx] + ' ' + right)
        return res