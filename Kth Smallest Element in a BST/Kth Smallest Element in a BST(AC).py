# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cursor = root
        stack = []
        inorderlist = []
        while len(stack) or cursor:
            while cursor:
                stack.insert(0,cursor)
                cursor = cursor.left
            cursor =  stack.pop(0)
            inorderlist.append(cursor.val)
            cursor = cursor.right
        return inorderlist[k-1]