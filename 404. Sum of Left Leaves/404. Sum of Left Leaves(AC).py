# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        stack.append(root)
        res = 0
        last = None
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if last and last.left == node:
                    #print(node.val)
                    res += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            last = node
        return res