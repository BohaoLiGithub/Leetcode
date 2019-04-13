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
        queue = collections.deque()
        queue.append((root,1))
        res = 1
        while queue:
            node,depth = queue.popleft()
            res = max(res,depth)
            for chi in node.children:
                queue.append((chi,depth+1))
        return res
        