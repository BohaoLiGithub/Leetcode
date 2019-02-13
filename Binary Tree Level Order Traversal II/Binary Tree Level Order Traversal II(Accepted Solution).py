# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res,0,root)
        return res
    def helper(self,res,level,root):
        if not root:
            return None
        if len(res) <= level:
            res.insert(0,[])
        res[len(res)-level-1].append(root.val)
        self.helper(res,level+1,root.left)
        self.helper(res,level+1,root.right)
            