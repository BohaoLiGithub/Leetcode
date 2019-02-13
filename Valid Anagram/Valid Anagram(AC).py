import operator
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = list(s)
        list2 = list(t)
        list1 = sorted(list1)
        list2 = sorted(list2)
        return operator.eq(list1,list2) 