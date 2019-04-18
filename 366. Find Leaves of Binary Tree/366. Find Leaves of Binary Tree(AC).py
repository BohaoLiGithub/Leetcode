# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.postOrder(root)
        return self.res
        
    def postOrder(self,root):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        max_depth = max(left,right) + 1
        if max_depth > len(self.res):
            self.res.append([])
        self.res[max_depth - 1].append(root.val)
        return max_depth