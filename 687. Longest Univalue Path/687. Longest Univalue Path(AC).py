# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# We go through the tree by post-order Traverse.
# We recursively calculate the max univalue in the root's left subtree and right subtree
# then we comapre the value of the visited node with the value of its left and right respectively.
# if the value is equal, then maxvalue + 1, otherwise 0
# then add up the two values and compare this value with the previous maximum value.
# at last, return the larger one
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 0
        self.helper(root)
        return self.ans
        
    def helper(self,root):
        if not root:
            return 0
        left_max = self.helper(root.left)
        right_max = self.helper(root.right)
        l,r = 0,0
        if root.left and root.left.val == root.val:
            l = 1 + left_max
        if root.right and root.right.val == root.val:
            r = 1 + right_max
        self.ans = max(self.ans,l+r)
        return max(l,r)
        