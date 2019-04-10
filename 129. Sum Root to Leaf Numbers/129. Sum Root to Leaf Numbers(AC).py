# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res
        stack = [(root,[root.val])]
        while stack:
            top,path_val = stack.pop(-1)
            if not top.left and not top.right:
                temp = 0
                for val in path_val:
                    temp = temp*10 + val
                res += temp
            if top.right:
                stack.append((top.right,path_val + [top.right.val]))
            if top.left:
                stack.append((top.left,path_val + [top.left.val]))
        return res