class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] >=0 and digits[-1] <=8:
            res = digits[:]
            res[-1] += 1
            return res
        else:
            flag = 1
            res = digits[:]
            res[-1] = 0
            #print(res)
            if len(res)>=2:
                for i in range(len(res)-2,-1,-1):
                    if res[i] == 9 and flag == 1:
                        res[i] = 0
                        flag =1
                    elif flag == 1:
                        res[i] += 1
                        break;
                if flag == 1 and res[0] == 0:
                    res.insert(0,1)
            else:
                res.insert(0,1)
            return res
