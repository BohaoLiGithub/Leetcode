# It is implemented by layer traversal
# The first node in the last layer is the result.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        level = 1
        queue = collections.deque()
        queue.appendleft((root,level))
        res = []
        while len(queue):
            top,topLevel = queue.pop()
            if len(res) < topLevel:
                res.append([top.val])
            else:
                res[topLevel-1].append(top.val)
            if top.left:
                queue.appendleft((top.left,topLevel+1))
            if top.right:
                queue.appendleft((top.right,topLevel+1))
        #print(res)
        return res[-1][0]