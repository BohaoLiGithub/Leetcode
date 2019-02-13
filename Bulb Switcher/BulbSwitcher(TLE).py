# 29/35 TLE

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        bulbList = list(0 for _ in range(n))
        for i in range(1,n+1):
            for j in range(i-1,n,i):
                self.switch(bulbList,j)
            #print (bulbList)
        res = 0
        for i in range(0,n):
            if bulbList[i] == 1:
                res += 1
        return res

    def switch(self,bulbList, index):
        if bulbList[index] == 0:
            bulbList[index] = 1
        else:
            bulbList[index] = 0