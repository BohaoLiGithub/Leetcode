# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('-inf')
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        pl = max(left,0)
        pr = max(right,0)
        ans = pl + pr + root.val
        self.res = max(self.res,ans)
        return max(pl,pr)+root.val