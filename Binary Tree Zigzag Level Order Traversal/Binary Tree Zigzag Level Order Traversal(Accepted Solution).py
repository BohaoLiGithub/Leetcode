# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root,res,0)
        return res
    def helper(self,root,res,level):
        if not root:
            return None
        if len(res) <= level:
            res.append([])
        if level%2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)
        self.helper(root.left,res,level+1)
        self.helper(root.right,res,level+1)