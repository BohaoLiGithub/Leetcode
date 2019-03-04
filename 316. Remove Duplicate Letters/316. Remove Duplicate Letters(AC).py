class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        countList = [0] *26
        boolList = [False] * 26
        for c in s:
            countList[ord(c)-ord('a')] +=1
        stack = []
        for c in s:
            countList[ord(c) - ord('a')] -= 1
            if boolList[ord(c) - ord('a')]:
                continue
            while len(stack) and c < stack[-1] and countList[ord(stack[-1]) - ord('a')] > 0:
                boolList[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(c)
            boolList[ord(c)-ord('a')] = True
        return ''.join(stack)