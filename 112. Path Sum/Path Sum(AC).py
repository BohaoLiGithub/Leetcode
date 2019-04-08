# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return
        val = root.val
        if val == sum and (not root.left and not root.right):
            if not root.left and not root.right:
                return True
            else:
                return False
        else:
            return self.hasPathSum(root.left,sum-val) or self.hasPathSum(root.right,sum-val)