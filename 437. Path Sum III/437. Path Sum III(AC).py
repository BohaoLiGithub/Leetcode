# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.mem = collections.defaultdict()
        self.result = 0
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        stack = []
        if not root:
            return 0
        stack.append(root)
        while stack:
            node = stack.pop()
            self.DFS(node,s,0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return self.result
    def DFS(self,node,s,temp_sum):
        if not node:
            return
        temp_sum += node.val
        if temp_sum == s:
            self.result += 1
        self.DFS(node.left,s,temp_sum)
        self.DFS(node.right,s,temp_sum)