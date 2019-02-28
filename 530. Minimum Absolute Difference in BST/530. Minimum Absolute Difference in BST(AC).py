# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        list_ = list()
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            list_.append(node.val)
            inorder(node.right)
        inorder(root)
        min_ = float('inf')
        for i in range(1,len(list_)):
            min_ = min(min_,list_[i]-list_[i-1])
        return min_