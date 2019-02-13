# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cursor = root
        depth = 1
        if cursor.left and cursor.right:
            depth += min(self.minDepth(cursor.left),self.minDepth(cursor.right))
        elif cursor.left:
            depth += self.minDepth(cursor.left)
        elif cursor.right:
            depth += self.minDepth(cursor.right)
        return depth