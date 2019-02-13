# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.insert(0,root)
        cursor = None
        while len(stack):
            cursor= stack.pop(0)
            res.append(cursor.val)
            if cursor.right:
                stack.insert(0,cursor.right)
            if cursor.left:
                stack.insert(0,cursor.left)
        return res