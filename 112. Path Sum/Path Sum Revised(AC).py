# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, m):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        val = root.val
        if not root.left and not root.right and val == m:
            return True
        else:
            res1 = self.hasPathSum(root.left,m-val)
            if not res1:
                res2 = self.hasPathSum(root.right,m-val)
                return res2
            else:
                return True