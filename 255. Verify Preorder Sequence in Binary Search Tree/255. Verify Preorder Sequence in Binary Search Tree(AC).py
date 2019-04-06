class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = float('-inf')
        stack = []
        for var in preorder:
            if var < lower:
                return False
            while len(stack) and var > stack[-1]:
                lower = stack.pop()
            stack.append(var)
        return True