# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return
        a = p.val
        b = q.val
        cursor = root
        while cursor:
            if cursor.val == a or cursor.val == b:
                return cursor
            elif cursor.val > a and cursor.val > b:
                cursor = cursor.left
            elif cursor.val < a and cursor.val < b:
                cursor = cursor.right
            else:
                return cursor