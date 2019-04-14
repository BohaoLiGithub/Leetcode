# 28/39


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
            if right in self.mem:
                if self.mem[right]:
                    list_.append(right)
                    print(list_)
                    self.helper(left,wordDict,list_)
            else:
                if right in wordDict:
                    self.mem[right] = True
                    list_.append(right)
                    print(list_)
                    res = self.helper(left,wordDict,list_)
        print(self.mem)
        return self.result
                        
    def helper(self,s,wordDict,list_):
        if s in self.mem:
            print(s),
            print(self.mem[s])
            return self.mem[s]
        result = False
        orig_list = list(list_)
        print('orig_list:')
        print(orig_list)
        print('end')
        for idx in range(len(s)):
            list_ = list(orig_list)
            right = s[idx:]
            left = s[:idx]
            if right in self.mem:
                if self.mem[right]:
                    list_.append(right)
                    print("else 2")
                    print(list_)
                    print(left)
                    res = self.helper(left,wordDict,list_)
                    if res:
                        if left == '': ##### 判定有问题
                            print('add:1233======:')
                            print(list_[::-1])
                            print('==============')
                            self.result.append(' '.join(list_[::-1]))
                        result = True
                    else:
                        self.mem[left] = False
            else:
                if right in wordDict:
                    self.mem[right] = True
                    print("else 1")
                    list_.append(right)
                    print(list_)
                    res = self.helper(left,wordDict,list_)
                    if res:
                        if left =='':
                            print('add======:')
                            print(list_[::-1])
                            self.result.append(' '.join(list_[::-1]))
                            print('-==============')
                        result = True
                    else:
                        self.mem[left] = False
                else:
                    self.mem[right] = False
        return result
                