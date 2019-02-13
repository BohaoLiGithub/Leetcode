class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        listA = list(s)
        listPL = ['(','[','{']
        listPR = [')',']','}']
        stack = []
        for i in listA:
            if i in listPL:
                stack.insert(0,i)
            elif i in listPR:
                if len(stack) == 0:
                    return False
                else:
                    res = stack.pop(0)
                    if i == ')' and res != '(':
                        return False
                    elif i == ']' and res != '[':
                        return False
                    elif i == '}' and res != '{':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False