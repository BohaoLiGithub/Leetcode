class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        cursor1,cursor2, num = 0,0,0
        while cursor1 != len(s):
            while cursor2 != len(t):
                if s[cursor1] == t[cursor2]:
                    num += 1
                    cursor2 += 1
                    break
                cursor2 += 1
            if cursor2 == len(t):
                break
            cursor1 += 1
        return True if num == len(s) else False