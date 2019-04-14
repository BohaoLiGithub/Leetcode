# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cum = 0
        self.helper(root)
        return root
    def helper(self,root):
        if not root:
            return
        self.helper(root.right)
        root.val += self.cum
        self.cum = root.val
        self.helper(root.left)
        