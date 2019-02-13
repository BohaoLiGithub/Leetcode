class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = list(num1)
        list1.reverse()
        #print(list1)
        list2 = list(num2)
        list2.reverse()
        #print(list2)
        res = list()
        add_one = 0
        if len(list1) > len(list2):
            for _ in range(len(list1)-len(list2)):
                list2.append('0')
        elif len(list1) < len(list2):
            for _ in range(len(list2)-len(list1)):
                list1.append('0')
        length = len(list1)
        for i in range(length):
            sum_ = int(list1[i]) + int(list2[i]) + add_one
            if sum_ >= 10:
                res.append(str(sum_%10))
                add_one = 1
            else:
                res.append(str(sum_))
                add_one = 0
        if add_one == 1:
            res.append(str(1))
        res.reverse()
        return ''.join(res)