# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.helper(root.left,root.right)
        
    def helper(self,L,R):
        if L and R and L.val == R.val:
            return self.helper(L.left,R.right) and self.helper(L.right,R.left)
        return not L and not R