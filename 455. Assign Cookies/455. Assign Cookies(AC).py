class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)#greed factor
        s.sort(reverse=True)#cookie size
        res = 0
        cur1 = 0 #cookie
        cur2 = 0 # child
        print(min(len(g),len(s)))
        while cur1 < len(s) and cur2 < len(g):
            if s[cur1] >= g[cur2]:
                res += 1
                cur1 += 1
                cur2 += 1
            else:
                cur2+=1
        return res