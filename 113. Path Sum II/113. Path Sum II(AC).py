# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, m):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = []
        stack.append((root,[root.val]))
        cur = None
        sum_ = sum
        while stack:
            cur,ls = stack.pop()
            #print(ls)
            if not cur.left and not cur.right and sum(ls) == m:
                res.append(ls)
            if cur.right:
                stack.append((cur.right,ls+[cur.right.val]))
            if cur.left:
                stack.append((cur.left,ls+[cur.left.val]))
        return res
            