# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        root.left = None
        
        self.flatten(left)
        self.flatten(right)
        root.right = left
        cursor = root
        while cursor.right:
            cursor = cursor.right
        cursor.right = right