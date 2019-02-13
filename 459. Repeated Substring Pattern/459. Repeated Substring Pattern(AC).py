class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        divisors = [i for i in range(1,len(s)) if len(s) % i == 0]
        #print(divisors)
        divisors = divisors[::-1]
        for j in divisors:
            if s.count(s[:int(j)]) == len(s) / j :
                return True
        return False
        