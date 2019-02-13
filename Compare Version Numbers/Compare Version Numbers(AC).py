class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == '' or version2 == '':
            return
        list1 = version1.split('.')
        list2 = version2.split('.')
        length = len(list1) if len(list1) <= len(list2) else len(list2)
        for i in range(length):
            if int(list1[i]) > int(list2[i]):
                return 1
            elif int(list1[i]) < int(list2[i]):
                return -1
        if len(list1) == len(list2):
            return 0
        elif len(list1) > len(list2):
            sum = 0
            for i in range(len(list2),len(list1)):
                sum += int(list1[i])
            if sum == 0:
                return 0
            else:
                return 1
        else:
            sum = 0
            for i in range(len(list1),len(list2)):
                sum += int(list2[i])
            if sum == 0:
                return 0
            else:
                return -1