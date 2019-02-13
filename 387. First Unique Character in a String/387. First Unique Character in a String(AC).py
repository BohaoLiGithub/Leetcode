class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = [chr(x) for x in range(ord('a'),ord('z')+1)]
        return min([s.index(i) for i in list1 if s.count(i) == 1] or [-1])