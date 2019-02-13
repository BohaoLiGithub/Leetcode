import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        nums = 1 #add 2
        for i in range(3,n):
            flag = True
            for j in range(2,int(math.ceil(math.sqrt(i)))+1):
                if i % j == 0:
                    flag = False
                    break;
            if flag:
                nums += 1       
        return nums