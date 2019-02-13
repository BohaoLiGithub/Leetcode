# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root,0,res)
        return res
    
    def helper(self,root,level,res):
        if not root:
            return 0
        if len(res) == level:
            res.append(root.val)
        self.helper(root.right,level+1,res)
        self.helper(root.left,level+1,res)