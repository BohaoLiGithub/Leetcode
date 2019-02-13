class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = list(s) 
        list1.reverse()
        
        return "".join(list1)