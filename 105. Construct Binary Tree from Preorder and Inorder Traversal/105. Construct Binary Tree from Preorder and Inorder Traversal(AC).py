# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            head_val = preorder.pop(0)
            head = TreeNode(head_val)
            idx = inorder.index(head_val)
            head.left = self.buildTree(preorder,inorder[0:idx])
            head.right = self.buildTree(preorder,inorder[idx+1:])
            return head