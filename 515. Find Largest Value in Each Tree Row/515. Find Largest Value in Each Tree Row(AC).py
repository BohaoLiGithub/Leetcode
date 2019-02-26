# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        layer = []
        queue = collections.deque()
        queue.appendleft((root,1))
        while len(queue):
            top,level = queue.pop()
            if len(layer) < level:
                layer.append([top.val])
            else:
                layer[level-1].append(top.val)
            if top.left:
                queue.appendleft((top.left,level+1))
            if top.right:
                queue.appendleft((top.right,level+1))
        res = []
        for i in range(len(layer)):
            res.append(max(layer[i]))
        return res