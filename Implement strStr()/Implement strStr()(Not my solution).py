class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '': return 0
        if needle not in haystack: 
            return -1
        else:
            return len(haystack.split(needle)[0])