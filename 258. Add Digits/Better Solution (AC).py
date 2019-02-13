class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum1 = 0
            while num > 0:
                sum1 += num % 10
                num /= 10
            num = sum1
        return num