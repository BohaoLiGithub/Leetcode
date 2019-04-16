class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i,ch in enumerate(shortest):
            for str_ in strs:
                if str_[i] != ch:
                    return shortest[:i]
        return shortest