"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        for ch in root.children:
            temp = self.maxDepth(ch) + 1
            res = max(res,temp)
        return res
            