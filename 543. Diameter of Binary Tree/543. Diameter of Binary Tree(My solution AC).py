# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = 0
        queue = collections.deque()
        queue.appendleft(root)
        while len(queue) != 0:
            temp = queue.pop()
            if temp.left:
                queue.appendleft(temp.left)
            if temp.right:
                queue.appendleft(temp.right)
            if temp.left or temp.right:
                result = max(self.helper(temp),result)
        return result
    def helper(self,root):
        left_length = self.maxLength(root.left)
        right_length = self.maxLength(root.right)
        return left_length + right_length
    def maxLength(self,node):
        if not node:
            return 0
        left = self.maxLength(node.left)
        right = self.maxLength(node.right)
        return 1 + max(left,right)