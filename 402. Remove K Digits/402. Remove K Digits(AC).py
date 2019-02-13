class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'
        stack = []
        stack.append(num[0])
     
        for i in range(1,len(num)):
            print("for"+str(num[i]))
            if k == 0:
                stack.append(num[i])
            else:
                while len(stack):
                    top = stack[-1]
                    if int(top) > int(num[i]) and k != 0:
                        print("pop:" + str(stack.pop()))
                        k -= 1
                        if len(stack) == 0:
                            stack.append(num[i])
                            break
                    else:
                        print("add:"+str(num[i]))
                        stack.append(num[i])
                        break
        res =  ''.join(stack).lstrip('0')
        print(res)
        res = res[:len(res)-k]
        return res if res != '' else '0'