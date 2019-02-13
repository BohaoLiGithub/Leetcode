class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = s.split(' ')
        res = ''
        #print (list_)
        for str_ in list_:
            str_ = str_[::-1]
            res += str_
            res += ' '
        res = res[:len(res)-1]
        return res