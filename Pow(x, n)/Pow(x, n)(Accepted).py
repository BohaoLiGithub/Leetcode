class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n < 0:
                n = -n
                x = 1/x
                return x * pow(x,n-1)
            else:
                return x * pow(x,n-1)