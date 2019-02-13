# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        def getvalue(root):
            if root is None:
                return 0
            left = getvalue(root.left)
            right = getvalue(root.right)
            result.append(abs(left - right))
            return root.val + left + right
        getvalue(root)
        return sum(result)