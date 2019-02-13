class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ''
        cursor = 0
        while cursor < len(s):
            num = 0
            substr = ''
            if s[cursor].isdigit():
                num += int(s[cursor])
                cursor += 1
                while s[cursor].isdigit():
                    num = num * 10 + int(s[cursor])
                    cursor += 1
                stack.append(num)
            elif s[cursor].isalpha():
                while cursor < len(s):
                    if s[cursor].isalpha():
                        substr += s[cursor]
                    else:
                        break
                    cursor += 1
                if len(stack) > 0:
                    str_top = stack[-1]
                    if str_top.isalpha():
                        stack.pop()
                        str_top += substr
                        stack.append(str_top)
                    else:
                        stack.append(substr)
                else:
                    res += substr
            elif s[cursor] == '[':
                stack.append(s[cursor])
                cursor += 1
            elif s[cursor] == ']':
                substr = stack.pop(-1) # substr
                stack.pop(-1) #[
                num = stack.pop(-1)
                temp_res = self.helper(num,substr)
                if len(stack) > 0:
                    if stack[-1] == '[':
                        stack.append(temp_res)
                    else:
                        str_top = stack.pop(-1)
                        str_top += temp_res
                        stack.append(str_top)
                else:
                    res += temp_res
                cursor += 1
        return res
    def helper(self,num,substr):
        temp = ''
        for _ in range(num):
            temp += substr
        return temp