class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        print (num)
        if 0 <= num <= 9:
            return num
        list1 = list(str(num))
        sum1 = 0
        for i in list1:
            sum1 += int(i)
        return self.addDigits(sum1)